import "./LoadingScreen.css"
import loadingImage from "../../assets/images/loading.png"

function LoadingScreen(){
    return (
        <div className="ls-container">
            <img src={loadingImage} alt="Loading animation" className="ls-image-rotation"></img>
        </div>
    );
}

export default LoadingScreen