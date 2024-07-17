import { useState } from "react";
import Button from "@mui/material/Button";
import CloudUploadIcon from "@mui/icons-material/CloudUpload";
import { styled } from "@mui/material/styles";

const VisuallyHiddenInput = styled("input")({
  clip: "rect(0 0 0 0)",
  height: "1px",
  margin: "-1px",
  overflow: "hidden",
  padding: "0",
  position: "absolute",
  whiteSpace: "nowrap",
  width: "1px",
});

const ButtonContainer = styled("div")({
  display: "flex",
  gap: "20px",
  alignItems: "center",
  justifyContent: "center",
  width: "75vw",
  margin: "auto",
});

// eslint-disable-next-line react/prop-types
const FileUpload = ({ onFileChange, onSubmit }) => {
  const [selectedFileName, setSelectedFileName] = useState("");
  const [fileSelected, setFileSelected] = useState(false);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setSelectedFileName(file ? file.name : "");
    setFileSelected(true); // Set file selected state to true
    onFileChange(event); // Call parent handler
  };

  const handleSubmit = () => {
    onSubmit();
    setFileSelected(false);
  };
  return (
    <>
      <ButtonContainer>
        <VisuallyHiddenInput
          accept=".docx"
          id="contained-button-file"
          type="file"
          onChange={handleFileChange}
        />
        <label htmlFor="contained-button-file">
          <Button
            variant="contained"
            component="span"
            startIcon={<CloudUploadIcon />}
          >
            Upload
          </Button>
        </label>
        <Button variant="contained" color="primary" onClick={handleSubmit}>
          Submit
        </Button>
      </ButtonContainer>
      {fileSelected && (
        <p style={{ fontSize: "12px", textAlign: "center", marginTop: "5px" }}>
          Selected file: {selectedFileName}
        </p>
      )}
    </>
  );
};

export default FileUpload;
