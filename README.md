# Jarvis Groq Backend

## Deploy/update on Render
1. Open your existing GitHub repository connected to Render.
2. Replace its `main.py` with this `main.py`; keep `requirements.txt` (it is also included here).
3. Commit the changes to GitHub. Render should redeploy automatically.
4. Open Render → your `jarvisbackend` service → Environment.
5. Add `GROQ_API_KEY` with the secret key created at https://console.groq.com/keys .
6. Add `GROQ_MODEL` = `llama-3.3-70b-versatile` (if this model is available in your Groq account).
7. Remove `OPENAI_API_KEY` if you previously added it; this code does not use it.
8. Save changes and wait for deployment.

## Test
- `GET /health` should return `{"status":"ok"}`.
- Open `/docs`, expand `POST /chat`, click **Try it out**, and send:
  `{"message":"Hello Jarvis, introduce yourself"}`

## Important
Keep `GROQ_API_KEY` private. Set it only in Render Environment variables; never put it in Android code or public GitHub. Free-tier limits and model availability may change. This backend returns AI text only; the Android app still needs to send recognized speech to `/chat`.
