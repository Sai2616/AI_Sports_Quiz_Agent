import { useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../services/api";
import "./QuizForm.css";
import Loader from "./Loader";

function QuizForm() {

    const navigate = useNavigate();

    const [sport, setSport] = useState("Cricket");
    const [difficulty, setDifficulty] = useState("Easy");
    const [topic, setTopic] = useState("");
    const [numQuestions, setNumQuestions] = useState(5);
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e) => {

    e.preventDefault();

    setLoading(true);

    try {

        const response = await API.post("/generate-quiz", {
            sport,
            difficulty,
            topic,
            num_questions: numQuestions
        });

        navigate("/quiz", {
            state: {
                quiz: response.data.quiz
            }
        });

    }
    catch (error) {

        console.error(error);

        alert("Failed to generate quiz.");

    }
    finally {

        setLoading(false);

    }

};

if (loading) {
    return <Loader />;
}
    return (
        <form className="quiz-form" onSubmit={handleSubmit}>

            <div className="form-group">
                <label>Sport</label>

                <select
                    value={sport}
                    onChange={(e) => setSport(e.target.value)}
                >
                    <option>Cricket</option>
                    <option>Football</option>
                    <option>Basketball</option>
                    <option>Tennis</option>
                    <option>Badminton</option>
                </select>
            </div>

            <div className="form-group">
                <label>Difficulty</label>

                <select
                    value={difficulty}
                    onChange={(e) => setDifficulty(e.target.value)}
                >
                    <option>Easy</option>
                    <option>Medium</option>
                    <option>Hard</option>
                </select>
            </div>

            <div className="form-group">
                <label>Topic (Optional)</label>

                <input
                    type="text"
                    placeholder="Example: IPL Finals"
                    value={topic}
                    onChange={(e) => setTopic(e.target.value)}
                />
            </div>

            <div className="form-group">
                <label>Number of Questions</label>

                <select
                    value={numQuestions}
                    onChange={(e) => setNumQuestions(Number(e.target.value))}
                >
                    <option value={5}>5</option>
                    <option value={10}>10</option>
                    <option value={15}>15</option>
                </select>
            </div>

            <button type="submit">
                Generate Quiz
            </button>

        </form>
    );
}

export default QuizForm;