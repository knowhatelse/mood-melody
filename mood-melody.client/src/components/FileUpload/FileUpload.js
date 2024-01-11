import "./FileUpload.css";
import { useState } from "react";
import axios from 'axios'

function FileUpload({handleSongsData, handleLoadingScreen}) {
  const [file, setFile] = useState(null);

  function sendFile() {
    if (!file) {
      alert("No file was uploaded");
      return;
    }

    const fd = new FormData();
    fd.append('file', file);

    handleLoadingScreen(true);

    axios.post('http://localhost:5000/analyze', fd, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    })
    .then(response => {
      if(response.data === null) {
        alert("Image couldn't be analyzed");
      }
      handleSongsData(response.data)
    })
    .catch(err => alert(err.response.data.bad_request))
    .finally( () => {
      handleLoadingScreen(false)
    })
  }

  return (
    <div className="fu-content-holder">
      <div className="fu-header-container">
        <p className="fu-title">
          Upolad an image of you and get your Top 10 songs based on you emotion!
        </p>
      </div>
      <div className="fu-center-holder">
        <div className="fu-input-holder">
          {file === null ? (
            <label className="fu-input-label">
              <input
                type="file"
                className="fu-input"
                accept="image/*"
                onChange={(e) => {
                  setFile(e.target.files[0]);
                }}
              ></input>
              <span className="fu-text">Choose file</span>
            </label>
          ) : (
            <div className="fu-uploaded-file">
              File uploaded
            </div>
          )}
        </div>
      </div>
      <div className="fu-bottom-holder">
        <div className="fu-sent-image">
          <button className="fu-sent-button" onClick={sendFile}>
            Get recomended songs
          </button>
        </div>
      </div>
    </div>
  );
}

export default FileUpload;
