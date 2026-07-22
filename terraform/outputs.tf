output "public_ip" {

  value = aws_instance.github_analyzer.public_ip

}

output "instance_id" {

  value = aws_instance.github_analyzer.id

}

output "bucket_name" {

  value = aws_s3_bucket.github_analyzer_reports.bucket

}