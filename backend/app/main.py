from fastapi import FastAPI

app = FastAPI(
    title="Energy generation analytics API",
    description="API for analysing UK energy generation forecasts.",
    version="0.1.0"
)

@app.get("/api/health")
def health_check():
    return {
        "status_code": 200,
        "status": "ok",
        "service": "energy generation analytics"
    }


