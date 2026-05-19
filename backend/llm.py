import os
from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


SYSTEM_PROMPT = """
You are a senior software engineer reviewing pull requests.

Analyze the given code diff and return ONLY valid JSON.

Do NOT include explanations outside JSON.

JSON format:

{
  "summary": "short explanation of what changed",
  "risk_level": "LOW | MEDIUM | HIGH",
  "issues": [
    "list of potential bugs, risks, or problems"
  ],
  "suggestions": [
    "list of improvements or best practices"
  ]
}

Rules:
- Be precise and technical
- Focus on real bugs and risks
- If uncertain, explain in issues instead of guessing
"""


def review_pr(diff: str):
    try:
        response = client.chat.completions.create(
            model=os.getenv("LLM_MODEL"),
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": diff}
            ],
            temperature=0
        )
        content = response.choices[0].message.content
        content = content.replace("```json", "").replace("```", "")

        print(content)
        try:
            return json.loads(content)
        except Exception:
            return {
                "error": "Failed to parse JSON",
                "raw_output": content
            }

    except Exception as e:
        return {
            "error": str(e),
            "fallback": "GROQ unavailable, using mock review",
            "diff_length": len(diff)
        }