resource "aws_instance" "github_analyzer" {

  ami           = var.ami_id

  instance_type = var.instance_type

  iam_instance_profile = aws_iam_instance_profile.github_analyzer_profile.name

  vpc_security_group_ids = [
    aws_security_group.github_analyzer_sg.id
  ]

}