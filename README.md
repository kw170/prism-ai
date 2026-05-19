# 🧠 PR Detective

AI-powered pull request review and debugging assistant that analyzes code changes, detects risks, and explains them like a senior software engineer.

---

# 🚀 Overview

PR Detective helps engineers understand and review pull requests faster using an LLM-powered reasoning system over code diffs.

Instead of manually scanning large PRs, you can paste a diff and instantly get:

- Clear summaries of changes
- Risk analysis (security, logic, performance)
- Potential bugs and edge cases
- Suggestions for improvements
- Missing test detection

---

# 💡 Example

## Input (GitHub PR diff)

```diff
- if (user.isAdmin == true)
+ if (user.role == "admin")
```

## Output

### SUMMARY
Refactors admin permission check logic from boolean flag to role-based access control.

### RISK LEVEL
HIGH

### ISSUES
- Potential inconsistency if `role` is not validated server-side
- Possible privilege escalation if role is user-controlled

### SUGGESTIONS
- Validate role assignment on backend only
- Add unit tests for unauthorized role mutation cases

---

# 🎯 Why This Project?

Modern engineering teams spend significant time:

- Reviewing pull requests
- Understanding unfamiliar codebases
- Catching subtle bugs before production
- Debugging CI/test failures

PR Detective acts as an AI “senior engineer reviewer” that reduces cognitive load and improves code quality.

---

# ⚙️ Architecture (MVP)

```text
GitHub PR Diff
      ↓
FastAPI Backend
      ↓
LLM Reasoning Layer
      ↓
Structured Review Output
```

---

# 🧱 MVP Features

## Core
- Paste GitHub PR diff
- AI-generated PR summary
- Risk scoring (Low / Medium / High)
- Bug detection suggestions
- Improvement recommendations

---

# 🛣️ Roadmap

## MVP (Current)
- PR diff → AI review system

## v1 (Product Version)
- GitHub OAuth integration
- Automatic PR reviews on real repositories
- Structured JSON output
- Better diff chunking for large PRs

## v2 (Advanced Agent System)
- CI/CD failure debugging agent
- Automatic GitHub bot comments
- Repository-aware reasoning (RAG over full codebase)
- Multi-step reasoning agent workflow

---

# 🧠 Future Vision

PR Detective evolves into a full AI engineering assistant that can:

- Review code like a senior engineer
- Debug production issues using logs and CI failures
- Understand full repository context
- Reduce production bugs before deployment
- Assist engineers during incident response

---

# 🛠️ Tech Stack

- Python
- FastAPI
- OpenAI / Anthropic API
- GitHub API (v1+)
- Vector DB (future: pgvector / Chroma)
- React / Next.js (optional frontend)

---

# 📦 Setup

```bash
git clone <repo-url>
cd pr-detective

pip install -r requirements.txt
uvicorn backend.main:app --reload
```

---

# 🔐 Environment Variables

Create a `.env` file:

```bash
OPENAI_API_KEY=your_api_key_here
```

---

# 📌 Project Status

🚧 MVP in active development

Current focus:
- PR diff → AI review pipeline
- Improving structured reasoning quality
- Building reliable backend system

---

# 🤝 Goals

This project is designed to demonstrate:

- Real-world AI engineering ability
- Backend system design
- Practical LLM application (beyond chatbots)
- Agentic reasoning over code
- Production-style software thinking

---

# 📄 License

MIT (or update later)