dep-start:
	docker-compose up -d

dep-stop:
	docker-compose down

dep-logs:
	docker-compose logs -f