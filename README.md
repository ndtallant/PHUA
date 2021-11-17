# Postgres High Utilization Alert

This is a serverless application to collect and log
query information on a Postgres DB when its CPU
utilization is over a given threshold.


### Setup and Deploy
1. Install the AWS SAM CLI
1. Install Docker
1. Clone this repo
1. run `sam build`
1. run `sam deploy --guided`
1. Enter the prompted information on the DB, utilization threshold, Lambda security group, and subnet IDs.
1. When prompted, you may save the deployment information to a `samconfig.toml`

**Note:** If you saved information to a `samconfig.toml`, you may deploy 
with `sam deploy` or `sam deploy --config-env <env name>`


### Components
- Lambda Function to query the DB, defined in `lambda_func.py`
- A CloudWatch Alarm for high CPU utilization
- An SNS Topic to connect the alarm and the lambda function
- All resources and their defaults can be adjusted in `template.yml`


### Troubleshooting
- The alarm can be tested by running `test-alarm.sh <alarm name>`. The alarm state will reset on its own.
- The lambda function can be tested through the SAM CLI or through the AWS Lambda console
