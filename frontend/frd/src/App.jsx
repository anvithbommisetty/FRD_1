import { useState } from "react";
import FileUpload from "../Components/FileUpload";
import ErrorComponent from "../Components/ErrorComponent";
import LoadingComponent from "../Components/LoadingComponent";
import IframeContainer from "../Components/IframeComponent";
import "./App.css";
function App() {
  const [showLoading, setShowLoading] = useState(false);
  const [pdfUrl, setPdfUrl] = useState(null);
  const [file, setFile] = useState(null);
  const [error, setError] = useState(null);
  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };
  const handleNewfile = () => {
    setFile(null);
    setPdfUrl(null);
    setError(null);
    setShowLoading(false);
  };

  const handleUpload = async () => {
    if (!file) {
      setError("Please upload a file");
      return;
    }
    try {
      var data = new FormData();
      data.append("file", file);
      await setShowLoading(true);
      const rawResponse = await fetch("http://127.0.0.1:5000/test", {
        method: "POST",
        body: data,
      });
      if (rawResponse.ok) {
        const blob = await rawResponse.blob();
        const url = window.URL.createObjectURL(blob);
        setPdfUrl(url);
      } else {
        const errorData = await rawResponse.json();
        setError(errorData.message);
      }
    } catch (error) {
      setError(error.message);
    } finally {
      setShowLoading(false);
    }
  };

  return (
    <div className="container">
      {!pdfUrl && showLoading && <LoadingComponent />}
      {!pdfUrl && !showLoading && !error && (
        <>
          <p className="description">
            Upload Transcript and generate Functional Requirements Document
          </p>
          <FileUpload onFileChange={handleFileChange} onSubmit={handleUpload} />
        </>
      )}
      {error && <ErrorComponent error={error} handleNewFile={handleNewfile} />}
      {pdfUrl && !showLoading && (
        <IframeContainer pdfUrl={pdfUrl} handleNewfile={handleNewfile} />
      )}
    </div>
  );
}

export default App;
