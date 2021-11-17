
alarm_name=$1

aws cloudwatch set-alarm-state \
  --alarm-name "${alarm_name}" \
  --state-reason "Testing the PHUA Amazon Cloudwatch alarm" \
  --state-value ALARM
