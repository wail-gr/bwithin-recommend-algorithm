from fastapi import FastAPI, Request
from your_algorithm_file import generate_recommendation  # adapt to your function

app = FastAPI()

@app.post("/recommend")
async def recommend(request: Request):
    data = await request.json()
    user_query = data.get("query")
    user_profile = data.get("profile")  # includes history, likes, etc.
    result = generate_recommendation(user_query, user_profile)
    return {"result": result}
