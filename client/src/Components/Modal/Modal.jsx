import React from "react";

export default function Modal(props) {
  console.log(props);
  return (
    <div
      className="modal fade"
      id="staticBackdrop"
      data-bs-backdrop="static"
      data-bs-keyboard="false"
      tabIndex="-1"
      aria-labelledby="staticBackdropLabel"
      aria-hidden="true"
    >
      <div className="modal-dialog">
        <div className="modal-content">
          <div className="modal-header">
            <h1 className="modal-title fs-5" id="staticBackdropLabel">
              Pothole Analyisis
            </h1>
            <button
              type="button"
              className="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div className="modal-body">
            <p>
              Hight Edge Cracking :{" "}
              <span style={{ color: "red" }}>
                {props.data[0].HighEdgeCracking} Detected
              </span><br />
              <span style={{ }}>
                Area = {props.area[0].HighEdgeCracking} square pixels
              </span>{" "}
            </p>
            <p>
              High Pothole :{" "}
              <span style={{ color: "red" }}>
                {props.data[0].HighPothole} Detected
              </span><br />
              <span style={{ marginLeft: "" }}>
                Area = {props.area[0].HighPothole} square pixels
              </span>
            </p>
            <p>
              High Ravelling :{" "}
              <span style={{ color: "red" }}>
                {props.data[0].HighRavelling} Detected
              </span><br />
              <span style={{ }}>
                Area = {props.area[0].HighRavelling} square pixels
              </span>
            </p>
            <p>
              Low Edge Cracking :{" "}
              <span style={{ color: "red" }}>
                {props.data[0].LowEdgeCracking} Detected
              </span><br />
              <span style={{ }}>
                Area = {props.area[0].LowEdgeCracking} square pixels
              </span>
            </p>
            <p>
              Low Pothole :{" "}
              <span style={{ color: "red" }}>
                {props.data[0].LowPothole} Detected
              </span><br />
              <span style={{ }}>
                Area = {props.area[0].LowPothole} square pixels
              </span>
            </p>
            <p>
              Low Ravelling :{" "}
              <span style={{ color: "red" }}>
                {props.data[0].LowRavelling} Detected
              </span><br />
              <span style={{ }}>
                Area = {props.area[0].LowRavelling} square pixels
              </span>
            </p>
            <p>
              Medium Edge Cracking :{" "}
              <span style={{ color: "red" }}>
                {props.data[0].MediumEdgeCracking} Detected
              </span><br />
              <span style={{ }}>
                Area = {props.area[0].MediumEdgeCracking} square pixels
              </span>
            </p>
            <p>
              Medium Ravelling :{" "}
              <span style={{ color: "red" }}>
                {props.data[0].MediumRavelling} Detected
              </span><br />
              <span style={{ }}>
                Area = {props.area[0].MediumRavelling} square pixels
              </span>
            </p>
            <p>
              Medium Rutting :{" "}
              <span style={{ color: "red" }}>
                {props.data[0].MediumRutting} Detected
              </span><br />
              <span style={{ }}>
                Area = {props.area[0].MediumRutting} square pixels
              </span>
            </p>
          </div>
          <div className="modal-footer">
            <button
              type="button"
              className="btn btn-secondary"
              data-bs-dismiss="modal"
            >
              Close
            </button>
            <button type="button" className="btn btn-primary">
              Understood
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
