# IAMRole=AWSDistroOpenTelemetryRole
# ParameterKey=IAMRole,ParameterValue=${IAMRole}

aws cloudformation create-stack --stack-name sts-open-telemetry-collector-dev \
    --template-body file://aws-otel-ec2-deployment-cfn.yaml \
    --parameters ParameterKey=KeyName,ParameterValue="$AWS_EC2_SSH_KEY_NAME" \
    --capabilities CAPABILITY_NAMED_IAM \
    --region "${AWS_REGION}"