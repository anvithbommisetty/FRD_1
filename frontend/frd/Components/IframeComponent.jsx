import React from "react";
import Button from "@mui/material/Button";
import Box from "@mui/material/Box";

const IframeContainer = ({ pdfUrl, handleNewfile }) => {
  return (
    <Box display="flex" flexDirection="column" alignItems="center">
      <Button
        variant="contained"
        onClick={handleNewfile}
        style={{ marginBottom: "10px" }}
      >
        Upload New File
      </Button>
      <Box width="75vw" height="90vh">
        <iframe
          src={pdfUrl}
          title="PDF Viewer"
          style={{ width: "100%", height: "100%", border: "none" }}
        ></iframe>
      </Box>
    </Box>
  );
};

export default IframeContainer;
