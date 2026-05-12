# GitHub Analyzer

A GitHub profile comparison tool built with Flask, JavaScript, and the GitHub REST API.

Compare two developers side-by-side through custom scoring, language analysis, repository statistics, and dynamically generated developer summaries.

> to compare — commit histories have become personality traits.

---

## Features

- Compare two GitHub developers side-by-side
- Dynamic Codex Score system
- Real-time GitHub API integration
- Language distribution analysis
- Total stars, forks, followers, and repository statistics
- Dynamically generated developer summaries
- Badge generation system
- SessionStorage caching for faster rendering and reduced API calls
- Graceful error handling for invalid usernames and API issues

---

## Codex Score Formula

The Codex Score is calculated using a weighted scoring system:

- Star Power (25%) — total stars earned
- Community Impact (20%) — followers and forks
- Repository Consistency (20%) — number of public repositories
- Documentation Quality (20%) — repositories with descriptions
- Language Diversity (15%) — number of languages used

Final score is normalized to a value between 0–100.

---

## Tech Stack

### Backend
- Python
- Flask
- Requests
- Flask-CORS

### Frontend
- HTML
- CSS
- Vanilla JavaScript

### API
- GitHub REST API

---

## Project Structure

```text
project/
│
├── backend/
│   ├── main.py
│   ├── analyzer.py
│   ├── summarizer.py
│   └── github_client.py
│
├── frontend/
│   ├── index.html
│   ├── results.html
│   ├── style.css
│   ├── results.css
│   ├── results.js
│   └── bg.png
│
├── tests/
│   └── test_analyzer.py
│
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

## How To Run

```bash
git clone <repo-url>
cd github-analyzer

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python backend/main.py
```

Create a `.env` file in the project root:

```env
GITHUB_TOKEN=your_github_token
```

Then open:

```text
http://127.0.0.1:5000
```