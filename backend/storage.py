import boto3
import json
import logging
import os
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client("s3")
BUCKET_NAME = os.getenv("S3_BUCKET")


def upload_report(report, user1, user2):

    try:

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        filename = (
            f"reports/{timestamp}_{user1}_vs_{user2}.json"
        )

        report_json = json.dumps(
            report,
            indent=4
        )

        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=filename,
            Body=report_json,
            ContentType="application/json"
        )

        logging.info(
            f"Report uploaded successfully: {filename}"
        )

    except Exception as e:

        logging.error(
            f"Failed to upload report to S3: {e}"
        )

        raise