from fastapi import FastAPI
from llm import review_pr
from github import fetch_pr_diff
from schemas import PRRequest

app = FastAPI()


@app.post("/review")
def review(req: PRRequest):

    diff = fetch_pr_diff(req.pr_url)

    if not diff:
        return {"error": "Could not fetch PR diff"}

    result = review_pr(diff)

    return result