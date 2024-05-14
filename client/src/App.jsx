import { useState } from "react";
import Loader from "./Components/Loader/Loader";

import "./App.css";
import Modal from "./Components/Modal/Modal";

function App() {
  const [images, setImages] = useState([]);
  const [detectImage, setdetectImages] = useState(false);
  const [viewReport, setViewReport] = useState(false);
  const [BatchNo, setBatchNo] = useState(0);
  const [isLoading, setIsLoading] = useState(false);
  var [result, setResult] = useState([]);
  var [report, setReport] = useState([]);
  var [area, setArea] = useState([]);

  const handleFileChange = (event) => {
    const fileList = event.target.files;
    const fileArray = Array.from(fileList);
    setImages(fileArray);
  };

  async function uploadImages(event) {
    event.preventDefault();
    if (images.length === 0) {
      alert("Please select at least one image.");
      return;
    }

    const formData = new FormData();
    images.forEach((image, index) => {
      formData.append(`images`, image);
    });
    console.log(formData);
    try {
      const response = await fetch(
        "http://localhost:8000//user/images/upload",
        {
          method: "POST",
          body: formData,
        }
      );
      const responseData = await response.json();
      console.log(responseData);
      if ((responseData.uploaded = "true")) {
        console.log("Uploaded");
        setdetectImages(true);
        setBatchNo(responseData.batch);
      }
    } catch (error) {
      console.error("Error uploading files:", error);
      console.log(error.message);
    }
  }

  async function detectImages() {
    console.log("Detecting Images");
    setIsLoading(true);
    var data = {
      batch_no: BatchNo,
    };
    var detect = await fetch("http://localhost:8000/user/pothole/detect", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });
    var response = await detect.json();
    console.log(response);
    if (response.status == "true") {
      setIsLoading(false);
      setdetectImages(false);
      setViewReport(true);
      setReport(response.report);
      setArea(response.area)
    }

  }

  async function detectedImages() {
    var data = {
      batch_no: BatchNo,
    };
    var detect = await fetch("http://localhost:8000/user/pothole/detected", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });
    var resultData = await detect.json();
    console.log(resultData);

    setResult(resultData.images);
    console.log(result);
  }

  return (
    <>
      <div className="container">
        <center>
          <div className="mt-5">
            <h1>Pothole Detector</h1>
          </div>
        </center>
        <form
          onSubmit={uploadImages}
          encType="multipart/form-data"
          className="mt-5"
        >
          <div className="input-group mb-3">
            <input
              type="file"
              multiple
              className="form-control"
              name="images"
              id="fileInput"
              onChange={handleFileChange}
            />
            <input
              className="input-group-text btn btn-primary"
              type="submit"
              value="Upload"
            />
          </div>
        </form>

        {detectImage ? (
          <div>
            <h4 className="batchno" id="batchno">
              Batch No : {BatchNo}
            </h4>
            <button
              id="triggerButton"
              className="btn btn-danger mt-4"
              onClick={detectImages}
            >
              Detect Images
            </button>
          </div>
        ) : (
          <div></div>
        )}
        <center>
          <Loader isLoading={isLoading} />
        </center>
        {viewReport ? (
          <div
            className="d-flex justify-content-between"
            style={{ width: "250px" }}
          >
            <button
              id="report"
              className="btn btn-success mt-4"
              data-bs-toggle="modal"
              data-bs-target="#staticBackdrop"
            >
              View Report
            </button>
            <button
              id="resultBtn"
              className="btn btn-success mt-4"
              onClick={detectedImages}
            >
              View Results
            </button>
            <Modal data={report} area={area}/>
          </div>
        ) : (
          <div></div>
        )}
        {result.map((item, index) => (
          <div className="accordion mt-3" id="accordionExample">
            <div className="accordion-item">
              <h2 className="accordion-header">
                <button
                  className="accordion-button"
                  type="button"
                  data-bs-toggle="collapse"
                  data-bs-target="#collapseOne"
                  aria-expanded="true"
                  aria-controls="collapseOne"
                >
                  <span style={{color:"blue"}}>Image {item.name.split('/')[1]}</span>
                </button>
              </h2>
              <div
                id="collapseOne"
                className="accordion-collapse collapse show"
                data-bs-parent="#accordionExample"
              >
                <div class="accordion-body">
                  <img src={`http://localhost:8000/${item.url}`} alt="" />
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </>
  );
}

export default App;
