import os

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
from pydantic import BaseModel, Field

app = FastAPI(title="Jarvis AI (Groq)", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=8000)

@app.get("/")
def home():
    return {"status": "Jarvis is online", "provider": "Groq"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat")
def chat(data: ChatRequest):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise HTTPException(
            status_code=503,
            detail="GROQ_API_KEY is missing from server environment variables.",
        )

    try:
        client = OpenAI(
            api_key=api_key,
            base_url="https://api.groq.com/openai/v1",
        )
        response = client.chat.completions.create(
            model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are Jarvis, a helpful personal AI assistant. "
                        "Reply in the user's language, including Hindi and Hinglish. "
                        "Be concise, clear, and helpful."
                    ),
                },
                {"role": "user", "content": data.message},
            ],
            max_tokens=700,
        )
        reply = response.choices[0].message.content
        return {"reply": reply or "Sorry, I couldn't generate a reply."}

    except Exception as error:
        print(f"Groq AI request failed: {type(error).__name__}: {error}")
        raise HTTPException(
            status_code=502,
            detail="Groq request failed. Check the API key, model name, and Render logs.",
        ) from error
