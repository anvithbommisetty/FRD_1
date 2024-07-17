import React from "react";
import Button from "@mui/material/Button";
import { styled } from "@mui/system";

// Define a styled component for the error div

const ErrorContainer = styled("div")({
  backgroundColor: "#f8d7da", // Example background color for error
  color: "#721c24", // Example text color for error
  padding: "10px",
  borderRadius: "5px",
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
  flexDirection: "column",
  textAlign: "center",
  width: "75vw",
  margin: "auto", // Center horizontally
});

const ErrorComponent = ({ error, handleNewFile }) => {
  return (
    <ErrorContainer>
      <p>{error}</p>
      <Button variant="contained" onClick={handleNewFile}>
        Retry
      </Button>
    </ErrorContainer>
  );
};

export default ErrorComponent;
