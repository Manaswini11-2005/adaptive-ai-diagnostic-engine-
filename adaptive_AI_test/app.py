from fastapi import FastAPI
from database import questions_collection, sessions_collection
from adaptive_engine import update_ability
from study_plan import generate_study_plan
import random

app = FastAPI()


# Home route
@app.get("/")
def home():
    return {"message": "Adaptive AI Diagnostic Engine Running"}


# Start Test
@app.post("/start-test")
def start_test(user_id: str):

    session = {
        "user_id": user_id,
        "ability": 0.5
    }

    sessions_collection.insert_one(session)

    return {
        "message": "Test started",
        "ability": 0.5
    }


# Get next question based on ability
@app.get("/next-question")
def next_question(user_id: str):

    session = sessions_collection.find_one({"user_id": user_id})

    if not session:
        return {"error": "User session not found"}

    ability = session["ability"]

    question = questions_collection.find_one(
        {"difficulty": {"$gte": ability}}
    )

    if not question:
        questions = list(questions_collection.find())
        question = random.choice(questions)

    return {
        "question": question["question"],
        "options": question["options"],
        "difficulty": question["difficulty"]
    }


# Submit answer
@app.post("/submit-answer")
def submit_answer(user_id: str, answer: str, question: str):

    session = sessions_collection.find_one({"user_id": user_id})

    if not session:
        return {"error": "User session not found"}

    q = questions_collection.find_one({"question": question})

    if not q:
        return {"error": "Question not found"}

    correct = q["correct_answer"] == answer

    new_ability = update_ability(session["ability"], correct)

    sessions_collection.update_one(
        {"user_id": user_id},
        {"$set": {"ability": new_ability}}
    )

    return {
        "correct": correct,
        "new_ability": new_ability
    }


