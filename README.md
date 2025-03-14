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


Multi-Machine Setup for Communication Demonstration
	•	Machine A (Your Mac – acting as the Registrar and possibly hosting an additional microservice):
	•	Example IP: 10.150.12.167（run ifconfig | grep "inet " for mac to check your ip address）
	•	Runs registrar.py on port 3000.
	•	Runs an additional microservice on a different port (e.g., port 5001).
	•	Machine B (Teammate’s Mac – hosting the LLM Microservice):
	•	Example IP: 10.190.63.127
	•	Runs app.py on port 5000.(for example).
  Testing with Postman

Follow these steps using Postman to demonstrate the full communication flow:

1. Register the LLM Microservice (on Machine B)
	•	Method: POST
	•	URL: http://10.150.12.167:3000/register
	•	Headers:
	•	Content-Type: application/json
	•	Body (raw JSON):

  {
  "serviceName": "LLMMicroservice",
  "address": "http://10.190.63.127:5000"
  }

  •	Expected Response:

  {
  "status": "success",
  "message": "LLMMicroservice registered."
  }

  2. Verify Registered Services(this could be ran on both machine A or B)
	•	Method: GET
	•	URL: http://10.150.12.167:3000/services
	•	Expected Response:
  [
  {
    "serviceName": "LLMMicroservice",
    "address": "http://10.190.63.127:5000"
  }
  ]

  3. Proxy a Request to the LLM Microservice
	•	Method: POST
	•	URL: http://10.150.12.167:3000/proxy/LLMMicroservice
	•	Headers:
	•	Content-Type: application/json
	•	Body (raw JSON):
  {
  "text": "Hello from Machine A via Postman!"
  }

  4. Send a Heartbeat to Keep the Service Active
	•	Method: POST
	•	URL: http://10.150.12.167:3000/heartbeat
	•	Headers:
	•	Content-Type: application/json
	•	Body (raw JSON):
  {
  "serviceName": "LLMMicroservice"
  }

  •	Expected Response:
  {
  "status": "success",
  "message": "Heartbeat received."
  }

  5. (Optional) Test Auto-Removal
	•	Stop the LLM microservice on Machine B (press Ctrl+C).
	•	Wait 5 minutes.
	•	Method: GET
  • URL: http://10.150.12.167:3000/services
	•	Expected Response:
    []