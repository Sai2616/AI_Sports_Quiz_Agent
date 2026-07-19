import "./Loader.css";

function Loader() {
    return (
        <div className="loader-container">

            <div className="spinner"></div>

            <h2>Generating Quiz...</h2>

            <p>Please wait while AI prepares your quiz.</p>

        </div>
    );
}

export default Loader;