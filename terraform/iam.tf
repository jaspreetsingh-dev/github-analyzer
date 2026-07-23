resource "aws_iam_policy" "github_analyzer_s3_policy" {

  name = "github-analyzer-s3-policy"

  description = "Allow EC2 to upload reports to S3"

  policy = jsonencode({

    Version = "2012-10-17"

    Statement = [

      {

        Effect = "Allow"

        Action = [

          "s3:PutObject"

        ]

        Resource = "${aws_s3_bucket.github_analyzer_reports.arn}/*"

      }

    ]

  })

}

resource "aws_iam_role" "github_analyzer_role" {

  name = "github-analyzer-role"

  assume_role_policy = jsonencode({

    Version = "2012-10-17"

    Statement = [

      {

        Effect = "Allow"

        Principal = {

          Service = "ec2.amazonaws.com"

        }

        Action = "sts:AssumeRole"

      }

    ]

  })

}

resource "aws_iam_role_policy_attachment" "github_analyzer_attach" {

  role = aws_iam_role.github_analyzer_role.name

  policy_arn = aws_iam_policy.github_analyzer_s3_policy.arn

}

resource "aws_iam_instance_profile" "github_analyzer_profile" {

  name = "github-analyzer-profile"

  role = aws_iam_role.github_analyzer_role.name

}