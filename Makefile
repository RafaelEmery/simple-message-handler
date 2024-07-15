list-commands:
	@echo "Listing commands..."
	@grep '^[a-zA-Z0-9_-]*:' Makefile | cut -d ':' -f 1

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

test:
	pytest -v -x --cov=loafer_handler --cov-report=term

manual-run:
	@poetry run python -m loafer_handler --flag manual

run:
	@poetry run python -m loafer_handler