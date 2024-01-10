import "./FileUpload.css";

function FileUpload() {
  return (
    <div className="fu-content-holder">
      <div className="fu-header-container">
        <p className="fu-title">
          Upolad an image of you and get your Top 10 songs based on you emotion!
        </p>
      </div>
      <div className="fu-center-holder">
        <div className="fu-input-holder">
          <label className="fu-input-label">
            <input type="file" className="fu-input" accept="image/*"></input>
            <span className="fu-text">Choose file</span>
          </label>
        </div>
      </div>
      <div className="fu-bottom-holder">
        <div className="fu-sent-image">
          <button className="fu-sent-button">Get recomended songs</button>
        </div>
      </div>
    </div>
  );
}

export default FileUpload;
