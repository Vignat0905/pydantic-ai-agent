from fastapi import FastAPI
from pydantic import BaseModel
from agent import ask_agent

app = FastAPI()

class UserPrompt(BaseModel):
    query: str

@app.post("/chat")
def chat(prompt: UserPrompt):
    response = ask_agent(prompt.query)
    return {"response": response}
