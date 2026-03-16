from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os

OPENAI_KEY = "YOUR API KEY"

app = FastAPI(title="OpenAI Prototype")
client = OpenAI(api_key=OPENAI_KEY)

class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "chatbot online"}

@app.post("/chat")
async def chat(request: ChatRequest):
    response = await client.chat.completions.create(
        model="Enter Your model name",
        messages=[{"role": "user", "content": request.message}]
    )
    return {"response": response.choices[0].message.content}
