from fastapi import FastAPI

from schemas import PRRequest, LogRequest

from llm import review_pr
from github import fetch_pr_diff
from debugger import analyze_failure_logs

app = FastAPI()


@app.post("/review")
def review(req: PRRequest):

    diff = fetch_pr_diff(req.pr_url)

    if not diff:
        return {"error": "Could not fetch PR diff"}

    result = review_pr(diff)

    return result

@app.post("/debug")
def debug_logs(req: LogRequest):

    result = analyze_failure_logs(req.logs)

    return result