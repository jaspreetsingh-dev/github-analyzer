variable "aws_region" {
  description = "AWS region where GitHub Analyzer will be deployed"

  type = string

  default = "ap-south-1"
}

variable "instance_type" {
  description = "EC2 instance type"

  type = string

  default = "t3.micro"
}

variable "ami_id" {
  description = "Amazon Linux AMI ID"

  type = string
}