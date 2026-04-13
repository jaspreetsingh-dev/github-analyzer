# GitHub Profile Analyzer

A Python tool that analyzes any GitHub profile and returns stats, language breakdown, and a custom Codex Score.

## Features
- Fetches real GitHub data via the GitHub REST API
- Calculates total stars, forks, and language distribution
- Generates a custom Codex Score (0-100) based on a weighted formula
- Returns a narrative summary of the developer

## Codex Score Formula
- Star Power (25%) — total stars earned
- Community Impact (20%) — followers and forks
- Repo Consistency (20%) — number of public repositories
- Documentation (20%) — repos with descriptions
- Language Diversity (15%) — number of languages used

## How To Run

1. Clone the repo
2. Create a virtual environment and activate it
3. Install dependencies with pip install -r requirements.txt
4. Add your GitHub token to .env as GITHUB_TOKEN=your_token
5. Run python backend/main.py
6. Open http://127.0.0.1:5000 in your browser

## Tech Stack
- Python, Flask, Requests
- GitHub REST API
- HTML, CSS, JavaScript