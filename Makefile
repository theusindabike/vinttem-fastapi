run:
	docker compose down --volumes && docker compose up --build 

run_staging:
	docker compose -f docker-compose.staging.yaml down --volumes && docker compose -f docker-compose.staging.yaml up --build

run_aws:
	docker-compose -f docker-compose.aws.yaml down && docker-compose -f docker-compose.aws.yaml up --build

migrate:
	docker compose exec api alembic upgrade head

docker_exec:
	docker exec -it vinttem_api /bin/sh

tests:
	docker compose exec api pytest

lint:
	isort src tests --profile black	&& black src tests
