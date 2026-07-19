import Navbar from "../components/Navbar";
import QuizForm from "../components/QuizForm";

import "./Home.css";

function Home() {
  return (
    <>
      <Navbar />

      <div className="home-container">
        <div className="hero">

          <h1>AI Sports Quiz Generator</h1>

          <p>
            Generate intelligent sports quizzes using
            Retrieval-Augmented Generation (RAG),
            ChromaDB, and Gemini AI.
          </p>

          <QuizForm />

        </div>
      </div>
    </>
  );
}

export default Home;