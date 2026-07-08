from fastapi import FastAPI

app = FastAPI(
    title="Enterprise Multi-Agent RAG Platform",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to Enterprise Multi-Agent RAG Platform"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }