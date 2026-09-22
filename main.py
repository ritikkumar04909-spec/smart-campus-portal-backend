from fastapi import FastAPI

app = FastAPI(
    title="Smart Campus Portal API",
    description="Backend API for Smart Campus Portal",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Smart Campus Portal API is running",
        "status": "success"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }