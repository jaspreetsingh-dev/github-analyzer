# GitHub Analyzer

A cloud-enabled GitHub profile comparison application built with Flask, Python, JavaScript, AWS, and the GitHub REST API.

The application compares two GitHub developers, generates developer insights, calculates a custom Codex Score, and automatically stores comparison reports in Amazon S3 using IAM Roles and Boto3.

---

## Features

- Compare two GitHub developers side-by-side
- Dynamic Codex Score system
- GitHub REST API integration
- Language distribution analysis
- Repository statistics
- Developer summary generation
- Badge generation
- SessionStorage caching
- Error handling
- Automatic comparison report storage in Amazon S3
- IAM Role authentication (no hardcoded AWS credentials)

---

## Architecture

Browser

↓

Flask Application (EC2)

↓

GitHub REST API

↓

Comparison Engine

↓

Boto3

↓

IAM Role

↓

Amazon S3

---

## Codex Score Formula

The Codex Score is calculated using a weighted scoring system.

- Star Power (25%)
- Community Impact (20%)
- Repository Consistency (20%)
- Documentation Quality (20%)
- Language Diversity (15%)

The final score is normalized between 0 and 100.

---

## Tech Stack

### Backend

- Python
- Flask
- Requests
- Flask-CORS
- Boto3

### Frontend

- HTML
- CSS
- Vanilla JavaScript

### Cloud

- Amazon EC2
- Amazon S3
- IAM Roles
- Amazon VPC

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
│   ├── github_client.py
│   └── storage.py
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

---

## Environment Variables

Create a `.env` file in the project root.

```env
GITHUB_TOKEN=your_github_token
S3_BUCKET=your_bucket_name
```

---

## Running Locally

```bash
git clone <repo-url>

cd github-analyzer

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python backend/main.py
```

Open:

```
http://127.0.0.1:5000
```

---

## AWS Deployment Notes

The cloud version of the project was deployed using:

- Amazon EC2
- IAM Role for secure AWS authentication
- Amazon S3 for report storage

AWS credentials are **not** stored inside the application. The application authenticates to AWS using an IAM Role attached to the EC2 instance.