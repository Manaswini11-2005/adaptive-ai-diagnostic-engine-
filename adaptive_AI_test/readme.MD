# Adaptive AI Diagnostic Engine

An AI-driven adaptive diagnostic test system built using FastAPI and MongoDB.  
The system dynamically adjusts question difficulty based on student performance and generates a personalized study plan.

---

## Project Overview

This project simulates an adaptive testing engine similar to those used in standardized exams.  
The system tracks a student's ability level and selects the next question based on their performance.

---

## Features

- Adaptive difficulty adjustment
- MongoDB question storage
- User ability score tracking
- Personalized study plan generation
- REST API backend
- Clean modular backend architecture

---

## Tech Stack

- Python
- FastAPI
- MongoDB

---

## Database Design

Two MongoDB collections are used.

### Questions Collection
Stores GRE-style questions.

Fields:
- question
- options
- correct_answer
- difficulty (0.1 – 1.0)
- topic

### UserSession Collection
Tracks the student's progress.

Fields:
- user_id
- ability

---

## Adaptive Algorithm

The system begins with a baseline ability score of **0.5**.

After each response:

If the answer is **correct**

ability = ability + 0.1

If the answer is **incorrect**

ability = ability - 0.1

The next question is selected from MongoDB based on the difficulty closest to the updated ability score.

This allows the system to dynamically adjust question difficulty based on user performance.

---

## API Endpoints

### Start Test
POST /start-test

Creates a new user session with baseline ability score.

---

### Get Next Question
GET /next-question

Returns the next question based on the user's ability score.

---

### Submit Answer
POST /submit-answer

Evaluates the user's answer and updates the ability score.

---

### Study Plan
GET /study-plan

Generates a personalized study recommendation based on the user's ability level.

---

## Running the Project

Install dependencies

pip install -r requirements.txt

Run the backend server

uvicorn app:app --reload

Open API documentation

http://127.0.0.1:8000/docs

---

## AI Log

AI tools such as ChatGPT were used during development to assist with:

- Backend architecture design
- Debugging FastAPI errors
- Structuring MongoDB queries
- Designing the adaptive algorithm

However, the integration, testing, and debugging of the final system were completed manually.

---

## Author

Manaswini Kolupula  
Computer Science Engineering (AI & ML)