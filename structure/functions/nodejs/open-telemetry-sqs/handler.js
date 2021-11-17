const AWS = require("aws-sdk");
const sqs = new AWS.SQS({apiVersion: '2012-11-05'});

AWS.config.update({region: process.env.AWS_REGION});

module.exports.main = (event, context, callback) => {
    const region = process.env.AWS_REGION;
    const account_id = process.env.AWS_ACCOUNT_ID
    const queue_name = process.env.OPEN_TELEMETRY_QUEUE_NAME;

    const queue_url = 'https://sqs.' + region + '.amazonaws.com/' + account_id + '/' + queue_name

    const params = {
      QueueUrl: queue_url,
      DelaySeconds: 10,
      MessageAttributes: {
        Hello: {
            DataType: 'String',
            StringValue: 'World'
        }
      },
      MessageBody: "Foo Bar"
    };

    sqs.sendMessage(params, function(err, data) {
      if (err) {
        callback(null, {
            statusCode: 400,
            body: JSON.stringify({
                failed: err
            })
        });
      } else {
        callback(null, {
            statusCode: 200,
            body: JSON.stringify({
                sqsMessageId: data.MessageId
            })
        });
      }
    });
};
