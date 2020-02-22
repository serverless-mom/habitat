console.log("Loading function");
var AWS = require("aws-sdk");
exports.handler = function(event, context) {
    var eventText = JSON.stringify(event, null, 2);
    console.log("Received event:", eventText);
    var sns = new AWS.SNS();
    var params = {
        Message: "Congrats you did it 34 days",
        Subject: "YouDidIt",
        TopicArn: "arn:aws:sns:us-west-2:659026047955:YouDidIT"
    };
    sns.publish(params, context.done);
};