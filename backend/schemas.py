from pydantic import BaseModel

class PRRequest(BaseModel):
    pr_url: str

class LogRequest(BaseModel):
    logs: str

class ReportRequest(BaseModel):
    pr_url: str
    logs: str = None