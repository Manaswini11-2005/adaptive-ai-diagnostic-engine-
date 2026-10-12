# Adaptive AI Diagnostic Engine 🧠

An adaptive testing system built using Python, FastAPI, and MongoDB that adjusts question difficulty based on student performance and provides personalized study recommendations.

## 📌 Project Overview

The Adaptive AI Diagnostic Engine is designed to make assessments more personalized and effective.

Instead of giving every student questions at the same difficulty level, the system adjusts the difficulty according to the student's answers. Correct answers increase the student's ability score, while incorrect answers decrease it.

The project demonstrates how an adaptive assessment system can track student progress and support personalized learning.

## ✨ Features

* **Adaptive Difficulty:** Adjusts question difficulty based on student performance.
* **Ability Score Tracking:** Maintains a score representing the student's current estimated ability.
* **Question Management:** Stores questions, answer options, correct answers, topics, and difficulty levels in MongoDB.
* **Answer Evaluation:** Checks submitted answers and updates the student's ability score.
* **Personalized Study Recommendations:** Generates study suggestions based on the ability score.
* **REST API:** Provides endpoints for starting tests, retrieving questions, and submitting answers.

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Backend Framework:** FastAPI
* **Database:** MongoDB
* **API:** REST API
* **Server:** Uvicorn

## ⚙️ How It Works

1. A student starts a test, and the system initializes their ability score to `0.5`.
2. The system retrieves a question from the MongoDB database based on the student's ability score.
3. The student submits an answer.
4. The system checks whether the answer is correct.
5. If the answer is correct, the ability score increases by `0.1`. If incorrect, it decreases by `0.1`.
6. The score is restricted to a range between `0.1` and `1.0`.
7. The updated score is used to help select subsequent questions.

The project uses a rule-based adaptive mechanism rather than a trained machine-learning model.

## 🗄️ Database Design

The project uses two MongoDB collections.

### 1. Questions Collection

Stores the questions used in assessments.

| Field            | Description                        |
| ---------------- | ---------------------------------- |
| `question`       | Question text                      |
| `options`        | Available answer choices           |
| `correct_answer` | Correct answer                     |
| `difficulty`     | Question difficulty score          |
| `topic`          | Topic associated with the question |

### 2. Sessions Collection

Stores the student's assessment progress.

| Field     | Description                                    |
| --------- | ---------------------------------------------- |
| `user_id` | Unique identifier used for the student session |
| `ability` | Current estimated ability score                |

## 🔌 API Endpoints

The FastAPI application currently implements the following endpoints.

| Method | Endpoint         | Description                                         |
| ------ | ---------------- | --------------------------------------------------- |
| GET    | `/`              | Checks whether the application is running           |
| POST   | `/start-test`    | Creates a student session                           |
| GET    | `/next-question` | Retrieves a question based on the student's ability |
| POST   | `/submit-answer` | Evaluates an answer and updates the ability score   |

### Interactive API Documentation

FastAPI automatically provides interactive API documentation when the application is running.

Open:

`http://127.0.0.1:8000/docs`

## 📂 Project Structure

```text
adaptive_AI_test/
│
├── app.py
├── adaptive_engine.py
├── database.py
├── insert_questions.py
├── study_plan.py
├── requirements.txt
└── README.md
```

### File Descriptions

* `app.py` — Defines the FastAPI application and API endpoints.
* `adaptive_engine.py` — Contains the logic for updating ability scores.
* `database.py` — Establishes the MongoDB connection and selects collections.
* `insert_questions.py` — Inserts sample questions into the database.
* `study_plan.py` — Generates study recommendations based on ability scores.
* `requirements.txt` — Lists the Python dependencies required to run the project.

## 🚀 Installation and Setup

### Prerequisites

Install the following before running the project:

* Python 3.9 or later
* MongoDB Community Server
* pip

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/adaptive-ai-diagnostic-engine.git
```

Replace `YOUR-USERNAME` with your GitHub username.

Navigate to the project directory:

```bash
cd adaptive-ai-diagnostic-engine
```

### Step 2
