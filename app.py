from flask import Flask, request, jsonify
from flask_cors import CORS
from colorthief import ColorThief
from io import BytesIO

app = Flask(__name__)
CORS(app)

def rgb_to_name(rgb):
    r, g, b = rgb
    if r > 200 and g > 200 and b > 200:
        return "White"
    elif r < 50 and g < 50 and b < 50:
        return "Black"
    elif r > 100 and b > 100 and g < 100:
        return "Purple"
    elif b > r and b > g:
        return "Blue"
    elif r > b and r > g:
        return "Red"
    elif g > r and g > b:
        return "Green"
    return "Gray"

@app.route("/")
def home():
    return "Gasket AI with Color Detection is live!"

@app.route("/analyze-card", methods=["POST"])
def analyze_card():
    file = request.files.get("cardImage")
    if not file:
        return jsonify({"error": "No card image uploaded"}), 400

    try:
        image_stream = BytesIO(file.read())
        color_thief = ColorThief(image_stream)
        dominant_color = color_thief.get_color(quality=1)
        color_name = rgb_to_name(dominant_color)

        return jsonify({
            "result": f"Suggested gasket color: {color_name} (RGB: {dominant_color})"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
