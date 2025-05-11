from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Gasket AI Backend is live!"

@app.route("/analyze-card", methods=["POST"])
def analyze_card():
    file = request.files.get("cardImage")

    if not file:
        return jsonify({"error": "No card image uploaded"}), 400

    # Placeholder response (mock AI logic)
    return jsonify({"result": "Suggested gasket color: Navy Blue and Silver"})
