import json
import boto3
import os

client = boto3.client('sns')


def main(event, context):
    region = os.environ['AWS_REGION']
    account_id = os.environ['AWS_ACCOUNT_ID']
    topic_name = os.environ['OPEN_TELEMETRY_TOPIC_NAME']

    topic_arn = 'arn:aws:sns:' + region + ':' + account_id + ':' + topic_name

    response = client.publish(
        TargetArn=topic_arn,
        Message=json.dumps({'default': "Hello World Message"}),
        MessageStructure='json'
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": response
        })
    }


if __name__ == "__main__":
    main('', '')
