run:
	docker-compose down --volumes && docker-compose up --build 
migrate:
	docker-compose exec api alembic upgrade head
docker_exec:
	docker exec -it vinttem_api /bin/sh
