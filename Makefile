run:
	docker-compose down --volumes && docker-compose up --build 
migrate:
	docker-compose exec api alembic upgrade head
