from flask import Flask, request, jsonify, render_template
import subprocess

app = Flask(__name__)

# Route to handle the POST request from the frontend
@app.route('/process', methods=['POST'])
def process_text():
    data = request.json
    input_text = data.get("text", "")
    
    try:
        result = subprocess.run(
            ["ollama", "run", "llama3.2", input_text],
            text=True,
            capture_output=True
        )
        response = result.stdout.strip()
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)})

# Route to render the simple web interface
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)