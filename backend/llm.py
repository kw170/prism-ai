import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from prompts import SYSTEM_PROMPT
from parser import split_diff_by_file

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


def analyze_file_diff(file_diff: str):

    response = client.chat.completions.create(
        model=os.getenv("LLM_MODEL"),
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": file_diff}
        ],
        temperature=0.2
    )

    content = response.choices[0].message.content
    content = content.replace("```json", "").replace("```", "")

    try:
        return json.loads(content)
    except Exception:
        return {
            "summary": "Failed to parse",
            "risk_level": "UNKNOWN",
            "issues": [],
            "suggestions": []
        }


def review_pr(diff: str):

    file_diffs = split_diff_by_file(diff)

    results = []

    for file_diff in file_diffs:
        analysis = analyze_file_diff(file_diff)
        results.append(analysis)

    return {
        "files_reviewed": len(results),
        "reviews": results
    }