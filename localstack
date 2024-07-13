#!/bin/bash

echo "setting up sns topics"

awslocal sns \
create-topic --name order_canceled \
--region us-east-1
awslocal sns \
create-topic --name package_canceled \
--region us-east-1

echo "setting up sqs queues"

awslocal sqs \
create-queue --queue-name canceled_orders \
--region us-east-1

echo "subscribing queue to topics"

awslocal sns \awslocal sqs receive-message --queue-url http://localhost:4566/000000000000/canceled_orders
subscribe --topic-arn "arn:aws:sns:us-east-1:000000000000:order_canceled" \
--protocol sqs  \
--notification-endpoint arn:aws:sqs:us-east-1:000000000000:canceled_orders
