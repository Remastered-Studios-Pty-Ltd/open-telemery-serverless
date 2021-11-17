# Stackstate Open Telemetry

## Local Environment Setup

1) Environment Variables Required
   1) export `AWS_PROFILE=***`
   2) export `AWS_ACCESS_KEY_ID=***`
   3) export `AWS_SECRET_ACCESS_KEY=*** `
   4) export `AWS_REGION=eu-west-1`


2) Create a `virtual env` for this project for example `sts-open-telemetry-proof-case`


3) `pip install boto3`


## Serverless - AWS Structure

Run `serverless deploy` to deploy your changes


## Open Telemetry Collectors
### EC2
https://aws-otel.github.io/docs/setup/ec2
1) `cd otel-collector/ec2`
2) `./cloudformation-create.sh`

