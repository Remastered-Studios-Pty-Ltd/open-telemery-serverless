const AWS = require("aws-sdk");
AWS.config.update({region: process.env.AWS_REGION});

const lambda = new AWS.Lambda();

module.exports.main = (event, context, callback) => {
    var params = {
      FunctionName: 'sts-open-telemetry-dev-NodeJsOpenTelemetryTo', // the lambda function we are going to invoke
      InvocationType: 'RequestResponse',
      LogType: 'Tail',
      Payload: JSON.stringify({
        "name" : "hello-world",
        "age": "100"
      })
    };

    lambda.invoke(params, function(err, data) {
      if (err) {
        callback(null, {
            statusCode: 400,
            body: JSON.stringify({
                error: err
            })
        });
      } else {
        callback(null, {
            statusCode: 200,
            body: JSON.stringify({
                lambdaResponse: data
            })
        });
      }
    })
};
