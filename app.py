from fastapi import FastAPI
from pydantic import BaseModel

class Essay(BaseModel):
    essay: str

app = FastAPI()

@app.get("/")
def home():
    return {"status": "VIVAEd AI Grader is running!"}

def dummy_grade(text):
    return {"SL1": 3, "RL1": 4, "RL2": 2, "RL4": 3, "W": 4}

@app.post("/grade")
def grade(data: Essay):
    return dummy_grade(data.essay)
