# Jarvis AI Backend

## Deploy on Render
1. Extract this ZIP.
2. Upload the files inside `Jarvis_Python_Backend` to a GitHub repository.
3. In Render, create a **New Web Service** and connect that repository.
4. Build command: `pip install -r requirements.txt`
5. Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. In Render → Environment, add `OPENAI_API_KEY` with your secret API key.
7. Optional: set `OPENAI_MODEL` to `gpt-4.1-mini` if your API account has access.
8. Deploy, then open `/health` on your Render URL. Expected: `{"status":"ok"}`.
9. Open `/docs` to test `POST /chat`.

Example request body: `{"message":"Hello Jarvis"}`

## Security
Never put your real API key in this code, Android app, or public GitHub repository.
API usage may be billed separately from a ChatGPT subscription. Add authentication and
rate limiting before exposing this endpoint publicly beyond testing.

This backend returns AI replies only. Your Android app still needs to send recognized
speech text to `POST /chat`.
