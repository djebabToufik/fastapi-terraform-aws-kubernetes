import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI is running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)  # Ensure it listens on 0.0.0.0
