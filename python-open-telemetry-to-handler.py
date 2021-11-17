import json


def main(event, context):
    response = {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Go Serverless v1.0! Your function executed successfully!"
        })
    }

    return response


if __name__ == "__main__":
    main('', '')
