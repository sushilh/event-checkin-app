# Event Check-In App

## ✅ Features
- Check in attendees from a CSV file
- Persistent updates to the same file
- Works with a Flask + HTML frontend

## 🚀 Hosting on Render (Free)

### 1. Push to GitHub
Create a GitHub repo and upload all project files.

### 2. Deploy on Render
- Go to https://render.com
- Click **New Web Service**
- Connect your repo
- Set:
  - **Build Command:** `pip install -r requirements.txt`
  - **Start Command:** `gunicorn app:app`
- Select **Free tier**
- Click **Deploy**

## 🌐 Access the App
- https://your-app.onrender.com/ – frontend + backend
- API Endpoints:
  - GET /attendees
  - POST /checkin with `{ "email": "someone@example.com" }`