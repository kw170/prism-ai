from llm import analyze_file_diff
from parser import split_diff_by_file
from risk import compute_overall_risk, detect_sensitive_files
from debugger import analyze_failure_logs

def generate_engineering_report(diff: str, logs: str = None):

    # 1. Split PR into files
    file_diffs = split_diff_by_file(diff)

    file_reviews = []

    for file_diff in file_diffs:
        review = analyze_file_diff(file_diff)

        review["sensitive_areas"] = detect_sensitive_files(file_diff)

        file_reviews.append(review)

    # 2. Overall PR risk
    overall_risk = compute_overall_risk(file_reviews)

    # 3. CI debugging (optional)
    ci_analysis = None
    print("HERE")
    print(logs)
    print("HERE")
    if logs:
        ci_analysis = analyze_failure_logs(logs)

    # 4. Final structured report
    return {
        "summary": "Engineering analysis of PR and system behavior",

        "pr_risk": overall_risk,

        "file_reviews": file_reviews,

        "ci_analysis": ci_analysis,

        "recommendation": generate_final_recommendation(
            overall_risk,
            ci_analysis
        )
    }

def generate_final_recommendation(risk, ci_analysis):

    if risk == "HIGH":
        return "DO NOT MERGE — high risk changes detected"

    if ci_analysis and ci_analysis.get("deployment_risk") == "HIGH":
        return "DO NOT DEPLOY — CI failures indicate system instability"

    if risk == "MEDIUM":
        return "MERGE WITH CAUTION — requires additional testing"

    return "SAFE TO MERGE"