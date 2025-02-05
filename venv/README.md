# Flask Microservice for LLM Interaction

This project is a simple Flask-based microservice that interacts with a locally installed Large Language Model (LLM) using Ollama. It allows users to send text input and receive responses from the LLM via both an API endpoint and a web interface.

---

## **Features**
- **POST API Endpoint**:
  - Send text input to the LLM using `/process`.
  - Receive JSON responses.
- **Web Interface**:
  - A simple webpage to send text and view responses directly in the browser.

---

## **Setup and Installation**
### **1. Prerequisites**
- Python 3.x installed.
- [Ollama](https://www.ollama.com/) installed with a compatible LLM (e.g., `llama3.2`).
- Docker (optional, for containerized deployments).

### **2. Clone the Repository**
```bash
git clone https://github.com/Volianwt/5590.git
cd ollama-flask-llm