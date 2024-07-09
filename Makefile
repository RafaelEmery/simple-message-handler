dep-start:
	docker-compose up -d

dep-stop:
	docker-compose down

dep-logs:
	docker-compose logs -f

localstack-bash:
	docker-compose exec localstack bash

publish-sample:
	@poetry run python message_publisher.py

run:
	poetry run python -m loafer_handler