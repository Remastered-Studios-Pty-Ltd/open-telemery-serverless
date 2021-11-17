const AWS = require("aws-sdk");
AWS.config.update({region: process.env.AWS_REGION});

const sns = new AWS.SNS({apiVersion: '2010-03-31'})

module.exports.main = (event, context, callback) => {
    const region = process.env.AWS_REGION;
    const account_id = process.env.AWS_ACCOUNT_ID
    const topic_name = process.env.OPEN_TELEMETRY_TOPIC_NAME;

    const topic_arn = 'arn:aws:sns:' + region + ':' + account_id + ':' + topic_name

    sns.publish({
      Message: JSON.stringify({
          'default': 'Hello World Message'
      }),
      TopicArn: topic_arn
    }).promise().then((data) => {
      callback(null, {
        statusCode: 200,
        body: JSON.stringify({
          message: data
        })
      });
    }).catch((err) => {
      callback(null, {
        statusCode: 400,
        body: JSON.stringify({
          error: err
        })
      });
    });
};
