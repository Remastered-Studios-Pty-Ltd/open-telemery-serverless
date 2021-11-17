## Local Environment Setup

1) Environment Variables Required
   1) `export AWS_PROFILE=***`
   2) `export AWS_ACCESS_KEY_ID=***`
   3) `export AWS_SECRET_ACCESS_KEY=*** `
   4) `export AWS_REGION=eu-west-1`

2) Create a `virtual env` for this project for example `sts-open-telemetry-proof-case`

3) `pip install boto3`


## Serverless - AWS Structure

Run `serverless deploy` to deploy your changes

After you deploy the serverless stack edit the `https://*.execute-api.eu-west-1.amazonaws.com` urls in the `collector.yaml`
to reflect the API endpoint shown after the serverless command completed. (Did not automate this) and rerun `serverless deploy` to deploy the config file again.


## Open Telemetry Config

File: `collector.yaml`

Exporter: otlphttp