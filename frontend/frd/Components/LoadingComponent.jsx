import CircularProgress from "@mui/material/CircularProgress";
import { styled } from "@mui/system";

// Define a styled component for the loading div
const LoadingContainer = styled("div")({
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
  flexDirection: "column",
  padding: "20px",
});

const LoadingComponent = () => {
  return (
    <LoadingContainer>
      <CircularProgress />
      <p style={{ marginTop: "10px", fontFamily: "Arial, sans-serif" }}>
        Processing...
      </p>
    </LoadingContainer>
  );
};

export default LoadingComponent;
