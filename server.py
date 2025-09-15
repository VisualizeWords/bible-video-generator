import requests
from flask import Flask, request, send_file, jsonify

app = Flask(__name__)

# 🔴 IMPORTANT: Update this with your Colab ngrok URL each time you restart Colab
COLAB_API_URL = "https://xxxx.ngrok-free.app/generate"

@app.route("/")
def home():
    return """
    <h2>Bible Story Video Generator</h2>

    <h3>Text Prompt → Video</h3>
    <form action="/generate-text" method="post">
        <input type="text" name="prompt" placeholder="Bible story prompt" required>
        <button type="submit">Generate</button>
    </form>

    <h3>Image + Description → Video</h3>
    <form action="/generate-image" method="post" enctype="multipart/form-data">
        <input type="text" name="description" placeholder="Describe the story" required><br><br>
        <input type="file" name="image" required><br><br>
        <button type="submit">Generate</button>
    </form>
    """

@app.route("/generate-text", methods=["POST"])
def generate_text():
    prompt = request.form.get("prompt")
    response = requests.post(COLAB_API_URL, data={"mode": "text", "prompt": prompt}, stream=True)

    if response.status_code == 200:
        video_file = "bible_text_video.mp4"
        with open(video_file, "wb") as f:
            for chunk in response.iter_content(8192):
                f.write(chunk)
        return send_file(video_file, as_attachment=True)
    return jsonify({"error": "Failed to generate text video"}), 500

@app.route("/generate-image", methods=["POST"])
def generate_image():
    description = request.form.get("description")
    response = requests.post(COLAB_API_URL, data={"mode": "image", "description": description}, stream=True)

    if response.status_code == 200:
        video_file = "bible_image_video.mp4"
        with open(video_file, "wb") as f:
            for chunk in response.iter_content(8192):
                f.write(chunk)
        return send_file(video_file, as_attachment=True)
    return jsonify({"error": "Failed to generate image video"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
