import json
import boto3

lambda_client = boto3.client('lambda')


def main(event, context):
    lambda_payload = json.dumps({
      "name": "hello-world",
      "age": "100"
    })

    invoke_response = lambda_client.invoke(
                         FunctionName='sts-open-telemetry-dev-PythonOpenTelemetryTo',
                         InvocationType='Event',
                         Payload=lambda_payload)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "World"
        })
    }


if __name__ == "__main__":
    main('', '')
