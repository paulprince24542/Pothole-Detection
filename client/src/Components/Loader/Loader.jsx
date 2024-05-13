import React from "react";
import "./loader.css"

export default function Loader(props) {
  return (
    <>
      {props.isLoading ? (
        <div className="boxes">
          <div className="box">
            <div></div>
            <div></div>
            <div></div>
            <div></div>
          </div>
          <div className="box">
            <div></div>
            <div></div>
            <div></div>
            <div></div>
          </div>
          <div className="box">
            <div></div>
            <div></div>
            <div></div>
            <div></div>
          </div>
          <div className="box">
            <div></div>
            <div></div>
            <div></div>
            <div></div>
          </div>
        </div> // Use CSS to style the loader
      ) : (
        <div>
        
        </div>
      )}
    </>
  );
}
