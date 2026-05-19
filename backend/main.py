from fastapi import FastAPI
from pydantic import BaseModel
from llm import review_pr

app = FastAPI()

class PRRequest(BaseModel):
    diff: str


@app.get("/")
def home():
    return {"status": "PR Detective running"}


@app.post("/review")
def review(req: PRRequest):
    result = review_pr(req.diff)
    return result