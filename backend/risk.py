RISK_SCORES = {
    "LOW": 1,
    "MEDIUM": 2,
    "HIGH": 3
}


SENSITIVE_KEYWORDS = [
    "auth",
    "login",
    "payment",
    "token",
    "admin",
    "database",
    "permission",
    "security"
]

# Calculates the average risk level from all files in the pr
def compute_overall_risk(reviews):

    total_score = 0

    for review in reviews:
        risk = review.get("risk_level", "LOW")
        total_score += RISK_SCORES.get(risk, 1)

    avg_score = total_score / max(len(reviews), 1)

    if avg_score >= 2.5:
        return "HIGH"
    elif avg_score >= 1.5:
        return "MEDIUM"

    return "LOW"

# Returns sensitive words in file
def detect_sensitive_files(diff_text: str):

    matches = []

    lower = diff_text.lower()

    for keyword in SENSITIVE_KEYWORDS:
        if keyword in lower:
            matches.append(keyword)

    return list(set(matches))