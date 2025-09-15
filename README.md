# Bible Story Video Generator

A simple web app that generates Bible story animations using AI.

## 🚀 Setup

1. **Google Colab Setup**
   - Open the provided Colab notebook.
   - Run the cells to start the AI video generator.
   - Copy the `ngrok` URL (looks like `https://xxxx.ngrok-free.app`).

2. **Update Server**
   - Open `server.py`.
   - Replace the `COLAB_API_URL` with your new Colab ngrok URL.

3. **Deploy to Render**
   - Push this repo to GitHub.
   - Create a new Web Service on [Render](https://render.com).
   - Set:
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn server:app`
   - Deploy → You’ll get a live site URL.

4. **Usage**
   - Open your Render app.
   - Enter a **text prompt** OR upload an **image + description**.
   - Wait ~30s → download your Bible animation video.
