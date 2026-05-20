import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from prompts import DEBUG_PROMPT

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def analyze_failure_logs(logs: str):

    response = client.chat.completions.create(
        model=os.getenv("LLM_MODEL"),
        messages=[
            {"role": "system", "content": DEBUG_PROMPT},
            {"role": "user", "content": logs}
        ],
        temperature=0.2
    )

    content = response.choices[0].message.content
    content = content.replace("```json", "").replace("```", "")

    try:
        return json.loads(content)
    except Exception:
        return {
            "error": "Failed to parse debugger output",
            "raw_output": content
        }