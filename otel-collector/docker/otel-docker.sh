PWD=$(pwd)

docker run --rm -p 4317:4317 -p 55680:55680 -p 8889:8888 \
  -e "AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}" \
  -e "AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}" \
  -e AWS_REGION="${AWS_REGION}" \
  -v "${PWD}/otel-local-config.yaml":/otel-local-config.yaml \
  --name awscollector public.ecr.aws/aws-observability/aws-otel-collector:latest \
  --config otel-local-config.yaml;