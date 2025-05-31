# Mini Docker Project

This is a simple Flask-based notes API built as a mini Docker project. It demonstrates:
- Creating a simple API with Flask
- Dockerizing the application with Dockerfile
- Running the application with Docker Compose

## 🚀 How to Run
```bash
docker compose up -d --build

Then open your browser at:
👉 http://localhost:5000

Or test with:
curl http://127.0.0.1:5000/
curl http://127.0.0.1:5000/notes
