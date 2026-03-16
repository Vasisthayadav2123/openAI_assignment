## How to Run the Prototype

### 1. Prerequisites
Ensure you have Python 3.8+ installed

### 2. Install Dependencies
Open your terminal and install the required Python packages:
`bash
pip install fastapi uvicorn openai pydantic
`

### 3. Configure the Code
Before starting the server, open your Python file (e.g., `main.py`) and update the following placeholders:
* **API Key:** Replace `"YOUR API KEY"` with your actual OpenAI API key.
* **Model:** Replace `"Enter Your model name"` with a valid model ID (e.g., `"gpt-4o"` or `"gpt-3.5-turbo"`).

### 4. Start the Server
Run the FastAPI application using Uvicorn.execute the following command in your terminal:
`bash
uvicorn main:app --reload
`
*(The `--reload` flag automatically restarts the server when you make code changes).*

### 5. Test the API
Once the server is running, you can interact with it using FastAPI's built-in Swagger UI. 
* Open your browser and navigate to: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* Expand the `POST /chat` endpoint, click **"Try it out"**, modify the JSON body with your message, and click **"Execute"**.
