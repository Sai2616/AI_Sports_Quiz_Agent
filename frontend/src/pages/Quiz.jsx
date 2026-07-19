import { useLocation, useNavigate } from "react-router-dom";
import { useState } from "react";
import "./Quiz.css";


function Quiz() {

    const location = useLocation();
    const navigate = useNavigate();

    const quiz = location.state?.quiz || [];

    const [currentQuestion, setCurrentQuestion] = useState(0);
const [selectedAnswer, setSelectedAnswer] = useState("");
const [score, setScore] = useState(0);
const [isFinished, setIsFinished] = useState(false);
const [showAnswer, setShowAnswer] = useState(false);
 const handleNext = () => {

    if (!showAnswer) {

        if (selectedAnswer === "") {
            alert("Please select an answer.");
            return;
        }

        if (selectedAnswer === question.answer) {
            setScore(prev => prev + 1);
        }

        setShowAnswer(true);
        return;
    }

    if (currentQuestion < quiz.length - 1) {

        setCurrentQuestion(prev => prev + 1);

        setSelectedAnswer("");

        setShowAnswer(false);

    } else {

        setIsFinished(true);

    }
};
    if (quiz.length === 0) {
        return (
            <div className="quiz-container">

                <h2>No Quiz Found</h2>

                <button onClick={() => navigate("/")}>
                    Go Back
                </button>

            </div>
        );
    }

    if (isFinished) {

    return (
        <div className="quiz-container">

            <h1>Quiz Completed 🎉</h1>

            <h2>
                Your Score: {score} / {quiz.length}
            </h2>

            <h3>
                Percentage: {((score / quiz.length) * 100).toFixed(0)}%
            </h3>

            <button onClick={() => navigate("/")}>
                Generate New Quiz
            </button>

        </div>
    );
}
    const question = quiz[currentQuestion];
    const progress = ((currentQuestion + 1) / quiz.length) * 100;

    return (
        <div className="quiz-container">

            <h1>AI Sports Quiz</h1>

            <h2>
                Question {currentQuestion + 1} / {quiz.length}
            </h2>

            <div className="progress-container">

    <div
        className="progress-bar"
        style={{ width: `${progress}%` }}
    ></div>

</div>

<p className="progress-text">
    {Math.round(progress)}% Completed
</p>

            <div className="question-card">

                <h3>{question.question}</h3>

                {
                    question.options.map((option, index) => (

                        <label
                            key={index}
    className={
        showAnswer
            ? option === question.answer
                ? "option correct"
                : option === selectedAnswer
                ? "option wrong"
                : "option"
            : "option"
    }
                        >

                            <input
                                type="radio"
                                name="answer"
                                value={option}
                                checked={selectedAnswer === option}
                                onChange={(e) =>
                                    setSelectedAnswer(e.target.value)
                                }
                            />

                            {option}
  {
    showAnswer && (

        <div className="explanation">

            <h3>Explanation</h3>

            <p>{question.explanation}</p>

        </div>

    )
}
                        </label>

                    ))
                }

            </div>

            <button
    onClick={handleNext}
    disabled={!selectedAnswer}
>
    {
        showAnswer
            ? currentQuestion === quiz.length - 1
                ? "Finish Quiz"
                : "Continue"
            : "Submit Answer"
    }
</button>

        </div>
        
    );
}

export default Quiz;