# GitHub Analyzer

A cloud-enabled GitHub profile comparison application built with Flask, Python, JavaScript, AWS, Terraform, and the GitHub REST API.

The application compares two GitHub developers, generates developer insights, calculates a custom Codex Score, and automatically stores comparison reports in Amazon S3 using IAM Roles and Boto3.

---

## Features

* Compare two GitHub developers side-by-side
* Dynamic Codex Score system
* GitHub REST API integration
* Language distribution analysis
* Repository statistics
* Developer summary generation
* Badge generation
* SessionStorage caching
* Error handling
* Automatic comparison report storage in Amazon S3
* IAM Role authentication (no hardcoded AWS credentials)
* Infrastructure provisioning with Terraform

---

## Architecture

```text
Browser
    │
    ▼
Flask Application (EC2)
    │
    ├──────────────► GitHub REST API
    │
    ▼
Comparison Engine
    │
    ▼
Boto3
    │
    ▼
IAM Role
    │
    ▼
Amazon S3
```

---

## Codex Score Formula

The Codex Score is calculated using a weighted scoring system.

* Star Power (25%)
* Community Impact (20%)
* Repository Consistency (20%)
* Documentation Quality (20%)
* Language Diversity (15%)

The final score is normalized between 0 and 100.

---

## Tech Stack

### Backend

* Python
* Flask
* Requests
* Flask-CORS
* Boto3

### Frontend

* HTML
* CSS
* Vanilla JavaScript

### Cloud

* Amazon EC2
* Amazon S3
* IAM Roles
* Amazon VPC
* Security Groups
* Terraform

### API

* GitHub REST API

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
├── terraform/
│   ├── providers.tf
│   ├── variables.tf
│   ├── terraform.tfvars
│   ├── ec2.tf
│   ├── iam.tf
│   ├── s3.tf
│   ├── security_group.tf
│   └── outputs.tf
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

## Terraform Configuration

Create a `terraform.tfvars` file inside the `terraform` directory.

Configure the following values before deployment:

```hcl
aws_region    = "your-region"
instance_type = "t3.micro"
ami_id        = "your-amazon-linux-ami"
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

```text
http://127.0.0.1:5000
```

---

## AWS Deployment Notes

The cloud infrastructure for this project is provisioned using Terraform.

Infrastructure includes:

* Amazon EC2
* Amazon S3
* IAM Roles
* Security Groups

Application deployment uses an EC2 instance with an IAM Role attached, allowing the application to upload comparison reports securely to Amazon S3 using Boto3.

AWS credentials are **never stored** inside the application. Authentication is performed automatically through the IAM Role attached to the EC2 instance.

---

## Future Improvements

* CloudWatch log integration
* Automated infrastructure deployment
* CI/CD pipeline with AWS CodePipeline
* Docker-based deployment
* HTTPS support
* Production monitoring and alerts
