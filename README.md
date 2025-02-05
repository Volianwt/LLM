# LLM Flask Microservice

This project is a Flask-based microservice that interacts with a locally installed Large Language Model (LLM) using Ollama. It provides a simple REST API and a web interface to send text input and receive responses from the LLM.

---

## **Features**
- **POST API Endpoint**: Send text to the LLM and receive responses via JSON.
- **Web Interface**: A user-friendly web page to interact with the LLM directly in a browser.

---

## **How to Run the Project**

### **Step 1: Prerequisites**
1. Install [Python 3.x](https://www.python.org/downloads/).
2. Install [Ollama](https://www.ollama.com/) and ensure it is working.
   - Verify by running:
     ```bash
     ollama list
     ```
   - Make sure you have the required LLM model (e.g., `llama3.2`). Install it using:
     ```bash
     ollama pull llama3.2
     ```

---

### **Step 2: Setup**
1. Clone this repository:
   ```bash
   git clone https://github.com/Volianwt/LLM.git
   cd LLM
2.（create a virtual environment  ）
python3 -m venv venv
source venv/bin/activate

3.Install Flask:
pip install flask

Step 3: Run the Application:
	1.	Start the Flask application:
 python app.py

 	2.	The app will run locally at:
  •	API Endpoint: http://127.0.0.1:5000/process (for POST requests)
	•	Web Interface: http://127.0.0.1:5000/ (for browser interaction)

 How to Test

1. API Testing with Postman
	•	POST Endpoint: http://127.0.0.1:5000/process
	•	Request Body (JSON format):
{
    "text": "What is the capital of France?"
}

	•	Response:

{
    "response": "The capital of France is Paris."
}

2. Using the Web Interface
	1.	Open http://127.0.0.1:5000/ in your browser.
	2.	Enter text in the input box and click Send.
	3.	View the response directly on the page.
