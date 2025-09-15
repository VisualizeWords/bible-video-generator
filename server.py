import os
from flask import Flask, request, jsonify, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "videos"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return "✅ Bible Video Generator is running on Render with Flask + Gunicorn!"

# 1. Upload image + description = video (simulated)
@app.route("/generate_from_image", methods=["POST"])
def generate_from_image():
    if "image" not in request.files or "description" not in request.form:
        return jsonify({"error": "Please upload an image and description"}), 400

    image = request.files["image"]
    description = request.form["description"]

    filename = secure_filename(image.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    image.save(filepath)

    # Simulate video generation (create dummy video file)
    output_video = os.path.join(OUTPUT_FOLDER, f"{filename}.mp4")
    with open(output_video, "wb") as f:
        f.write(b"Fake video content for image + description: " + description.encode())

    return jsonify({
        "message": "Video generated successfully!",
        "download_url": f"/download/{filename}.mp4"
    })

# 2. Text prompt = video (simulated)
@app.route("/generate_from_text", methods=["POST"])
def generate_from_text():
    data = request.json
    if not data or "prompt" not in data:
        return jsonify({"error": "Please provide a text prompt"}), 400

    prompt = data["prompt"]

    # Simulate video generation (create dummy video file)
    output_video = os.path.join(OUTPUT_FOLDER, f"text_prompt.mp4")
    with open(output_video, "wb") as f:
        f.write(b"Fake video content for prompt: " + prompt.encode())

    return jsonify({
        "message": "Video generated successfully!",
        "download_url": "/download/text_prompt.mp4"
    })

# 3. Download endpoint
@app.route("/download/<filename>")
def download(filename):
    filepath = os.path.join(OUTPUT_FOLDER, filename)
    if os.path.exists(filepath):
        return send_file(filepath, as_attachment=True)
    return jsonify({"error": "File not found"}), 404
