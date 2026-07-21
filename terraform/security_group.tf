resource "aws_security_group" "github_analyzer_sg" {

  name        = "github-analyzer-sg"
  description = "Security group for GitHub Analyzer"

  ingress {
    description = "SSH"

    from_port = 22
    to_port   = 22

    protocol = "tcp"

    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Flask"

    from_port = 5000
    to_port   = 5000

    protocol = "tcp"

    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {

    from_port = 0
    to_port   = 0

    protocol = "-1"

    cidr_blocks = ["0.0.0.0/0"]
  }
}