import os
from typing import List, Optional, Dict
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()


HF_TOKEN = os.getenv("HF_TOKEN")
DEFAULT_MODEL = os.getenv("HF_MODEL", "meta-llama/Llama-3.2-3B-Instruct")

if not HF_TOKEN:
    raise RuntimeError("HF_TOKEN environment variable not set")

app = FastAPI(title="Hugging Face LLM Prototype")
client = InferenceClient(model=DEFAULT_MODEL, token=HF_TOKEN)


chat_histories: Dict[str, List[Dict[str, str]]] = {}

class ChatRequest(BaseModel):
    message: str
    session_id: str = "default-user"
    system_prompt: str = "You are a helpful and concise AI assistant."
    model: Optional[str] = None
    temperature: float = 0.7
    max_tokens: int = 512

@app.get("/health")
async def health_check():
    """Confirms the API is running and the HF Token is present."""
    return {
        "status": "healthy",
        "model_configured": DEFAULT_MODEL,
        "token_set": bool(HF_TOKEN)
    }

@app.post("/chat")
async def chat(request: ChatRequest):
    try:

        target_model = request.model or DEFAULT_MODEL
        
        if request.session_id not in chat_histories:
            chat_histories[request.session_id] = [{"role": "system", "content": request.system_prompt}]
        
        history = chat_histories[request.session_id]
        history.append({"role": "user", "content": request.message})

        response = client.chat_completion(
            model=target_model,
            messages=history,
            temperature=request.temperature,
            max_tokens=request.max_tokens,
        )

        assistant_message = response.choices[0].message.content

        history.append({"role": "assistant", "content": assistant_message})

        return {
            "session_id": request.session_id,
            "model": target_model,
            "response": assistant_message,
            "history_length": len(history)
        }

    except Exception as e:
        error_msg = str(e)
        if "Authorization" in error_msg:
            raise HTTPException(status_code=401, detail="Invalid Hugging Face Token.")
        if "Model not found" in error_msg:
            raise HTTPException(status_code=404, detail=f"Model '{target_model}' not found or loading.")
        
        raise HTTPException(status_code=500, detail=error_msg)

@app.delete("/chat/{session_id}")
async def clear_history(session_id: str):
    """Utility to reset a conversation."""
    if session_id in chat_histories:
        del chat_histories[session_id]
        return {"message": f"History for {session_id} cleared."}
    raise HTTPException(status_code=404, detail="Session not found.")