<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

  <h1>Hugging Face LLM FastAPI Chat</h1>
  <p>A simple FastAPI service to chat with Hugging Face LLM models.</p>

  <h2>Setup</h2>

  <h3>1. Clone the repository</h3>
  <pre><code>git clone https://github.com/Vasisthayadav2123/openAI_assignment</code></pre>

  <h3>2. Create a virtual environment</h3>
  <pre><code>python -m venv venv
# Linux / macOS
source venv/bin/activate
# Windows
venv\Scripts\activate</code></pre>

  <h3>3. Install dependencies</h3>
  <pre><code>pip install fastapi uvicorn pydantic python-dotenv huggingface-hubt</code></pre>

  <h3>4. Configure environment variables</h3>
  <p>Create a <code>.env</code> file in the root directory:</p>
  <pre><code>HF_TOKEN=your_huggingface_api_token
HF_MODEL=meta-llama/Llama-3.2-3B-Instruct  # optional, default model</code></pre>

  <h2>Running the API</h2>
  <pre><code>uvicorn main:app --reload --host 0.0.0.0 --port 8000</code></pre>
  <ul>
    <li>The API will be available at: <a href="http://localhost:8000" target="_blank">http://localhost:8000</a></li>
    <li>Interactive docs at: <a href="http://localhost:8000/docs" target="_blank">http://localhost:8000/docs</a></li>
  </ul>

  <h2>Endpoints</h2>
  <ul>
    <li><strong>Health Check</strong>: <code>GET /health</code> – Verify API is running and token is set.</li>
    <li><strong>Chat</strong>: <code>POST /chat</code> – Send a message and get a response from the LLM.</li>
    <li><strong>Clear Chat History</strong>: <code>DELETE /chat/{'{session_id}'}</code> – Reset a conversation session.</li>
  </ul>

</body>
</html>
