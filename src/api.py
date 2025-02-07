from flask import Flask, request, jsonify
import threading

app = Flask(__name__)

logs = []

@app.route("/", methods=["GET"])
def home():
    logs.append("Endpoint '/' acessado")
    return jsonify({"message": "API está rodando!"})

@app.route("/data", methods=["POST"])
def receive_data():
    data = request.json
    logs.append(f"Recebido: {data}")
    return jsonify({"status": "success", "received": data})

def run_api():
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)
