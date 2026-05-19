import os
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3.diff"
}


def fetch_pr_diff(pr_url: str):
    """
    Converts GitHub PR URL → raw diff
    """

    # Example PR URL:
    # https://github.com/owner/repo/pull/1

    if not pr_url.endswith(".diff"):
        pr_url = pr_url + ".diff"

    response = requests.get(pr_url, headers=HEADERS)

    if response.status_code != 200:
        return None
    return response.text