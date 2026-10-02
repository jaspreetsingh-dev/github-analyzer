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

**Backend:** Python, Flask, Requests, Flask-CORS, Boto3

**Frontend:** HTML, CSS, Vanilla JavaScript

**Cloud:** Amazon EC2, Amazon S3, IAM Roles, Default VPC and Security Groups, Terraform

**API:** GitHub REST API

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
```

Activate the virtual environment:

```bash
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

Install dependencies and start the app:

```bash
pip install -r requirements.txt

python backend/main.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## Deployment

Terraform provisions an EC2 instance, an S3 bucket, an IAM Role and a Security Group in the default VPC.

The application runs on the EC2 instance with the IAM Role attached, which allows it to upload comparison reports to Amazon S3 using Boto3. AWS credentials are never stored inside the application.

Create a `terraform.tfvars` file inside the `terraform` directory:

```hcl
aws_region    = "your-region"
instance_type = "t3.micro"
ami_id        = "your-amazon-linux-ami"
```

Provision the infrastructure:

```bash
cd terraform
terraform init
terraform plan
terraform apply
```

Tear it down:

```bash
terraform destroy
```

---

## Status

The application was deployed on AWS EC2. It is not currently running. Screenshots are in the LinkedIn Featured section.
