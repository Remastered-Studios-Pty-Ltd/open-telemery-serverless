import json
import boto3
import os

sqs = boto3.client('sqs')


def main(event, context):
    region = os.environ['AWS_REGION']
    account_id = os.environ['AWS_ACCOUNT_ID']
    queue_name = os.environ['OPEN_TELEMETRY_QUEUE_NAME']

    queue_url = 'https://sqs.' + region + '.amazonaws.com/' + account_id + '/' + queue_name

    # List SQS queues
    response = sqs.send_message(
        QueueUrl=queue_url,
        DelaySeconds=10,
        MessageAttributes={
            'Hello': {
                'DataType': 'String',
                'StringValue': 'World'
            }
        },
        MessageBody=(
            'Foo'
            'Bar'
        )
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "sqsMessageId": response['MessageId']
        })
    }


if __name__ == "__main__":
    main('', '')
