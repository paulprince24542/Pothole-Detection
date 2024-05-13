import React from "react";

export default function Modal(props) {
    console.log(props)
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
            <p>Hight Edge Cracking : <span style={{color:"red"}}>{props.data[0].HighEdgeCracking}</span></p>
            <p>High Pothole : <span style={{color:"red"}}>{props.data[0].HighPothole}</span></p>
            <p>High Ravelling : <span style={{color:"red"}}>{props.data[0].HighRavelling}</span></p>
            <p>Low Edge Cracking : <span style={{color:"red"}}>{props.data[0].LowEdgeCracking}</span></p>
            <p>Low Pothole : <span style={{color:"red"}}>{props.data[0].LowPothole}</span></p>
            <p>Low Ravelling : <span style={{color:"red"}}>{props.data[0].LowRavelling}</span></p>
            <p>Medium Edge Cracking : <span style={{color:"red"}}>{props.data[0].MediumEdgeCracking}</span></p>
            <p>Medium Ravelling : <span style={{color:"red"}}>{props.data[0].MediumRavelling}</span></p>
            <p>Medium Rutting : <span style={{color:"red"}}>{props.data[0].MediumRutting}</span></p>
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
