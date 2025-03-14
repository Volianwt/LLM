from flask import Flask, request, jsonify
import time, requests

app = Flask(__name__)

# This dictionary will hold the registered services.
# The key is the service name, and the value is another dictionary with its address and last heartbeat time.
services = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    serviceName = data.get('serviceName')
    address = data.get('address')
    if serviceName and address:
        # Save the service details and current time (timestamp)
        services[serviceName] = {'address': address, 'lastHeartbeat': time.time()}
        return jsonify({"status": "success", "message": f"{serviceName} registered."})
    return jsonify({"error": "Invalid data"}), 400

@app.route('/services', methods=['GET'])
def list_services():
    # Return the list of active services
    service_list = [{"serviceName": name, "address": info['address']} for name, info in services.items()]
    return jsonify(service_list)

@app.route('/proxy/<serviceName>', methods=['POST'])
def proxy(serviceName):
    if serviceName not in services:
        return jsonify({"error": "Service not found"}), 404
    # Get the target service's address
    target = services[serviceName]['address']
    try:
        # Forward the request to the target service's '/process' endpoint
        response = requests.post(f"{target}/process", json=request.get_json())
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/heartbeat', methods=['POST'])
def heartbeat():
    data = request.get_json()
    serviceName = data.get('serviceName')
    if serviceName in services:
        # Update the lastHeartbeat time to current time
        services[serviceName]['lastHeartbeat'] = time.time()
        return jsonify({"status": "success", "message": "Heartbeat received."})
    return jsonify({"error": "Service not found."}), 404

# Function to remove inactive services (no heartbeat in 5 minutes)
def cleanup_services():
    current_time = time.time()
    to_remove = []
    for name, info in services.items():
        if current_time - info['lastHeartbeat'] > 300:  # 300 seconds = 5 minutes
            to_remove.append(name)
    for name in to_remove:
        del services[name]
        print(f"{name} removed due to timeout.")

if __name__ == '__main__':
    # Run cleanup every 60 seconds using a simple Timer
    from threading import Timer
    def schedule_cleanup():
        cleanup_services()
        Timer(60, schedule_cleanup).start()  # Repeat every minute
    schedule_cleanup()
    app.run(host='0.0.0.0', port=3000)
