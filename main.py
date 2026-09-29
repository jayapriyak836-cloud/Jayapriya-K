from fastapi import FastAPI

app = FastAPI(title="PocketSmart AI")

@app.get("/")
def home():
    return {"message": "PocketSmart AI is Running!"}

@app.get("/expenses")
def get_expenses():
    return {"expenses": [{"item": "Food", "amount": 100}]}

@app.post("/predict")
def predict(amount: float):
    if amount > 500:
        return {"prediction": "High spending!"}
    else:
        return {"prediction": "Good habit"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
