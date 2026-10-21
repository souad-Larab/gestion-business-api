
from fastapi import FastAPI

app= FastAPI(title = "Clinic API", version = "0.1.0") 

@app.get("/status")
def check_status():
    return {"status": "ok"}