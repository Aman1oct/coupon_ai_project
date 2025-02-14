from fastapi import FastAPI
from model import get_recommendations

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the AI Coupon API"}

@app.get("/recommend/{user_interest}")
def recommend(user_interest: str):
    return get_recommendations(user_interest)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
