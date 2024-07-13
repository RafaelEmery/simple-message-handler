dep-start:
	docker-compose up -d

dep-stop:
	docker-compose down

dep-logs:
	docker-compose logs -f

localstack-bash:
	docker-compose exec localstack bash

view-messages:
	docker-compose exec localstack awslocal sqs receive-message --queue-url http://localhost:4566/000000000000/canceled_orders

publish-sample:
	@poetry run python message_publisher.py

manual-run:
	@poetry run python -m loafer_handler --flag manual

run:
	@poetry run python -m loafer_handler