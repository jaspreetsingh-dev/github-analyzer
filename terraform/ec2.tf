resource "aws_instance" "github_analyzer" {

  ami = var.ami_id

  instance_type = var.instance_type

}