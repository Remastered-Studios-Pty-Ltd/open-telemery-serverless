import json
import boto3
from datetime import datetime

client = boto3.client('s3')


def main(event, context):
    now = datetime.now()

    target = "metric"
    bucket = "sts-open-telemetry-metrics"

    filename_event = now.strftime(target + "-event-%d-%m-%Y_%H-%M-%S.txt")
    client.put_object(ContentType="application/json", ACL="public-read", Body=json.dumps(event), Bucket=bucket, Key=filename_event)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Sample Trace Response"
        })
    }


if __name__ == "__main__":
    main('', '')
