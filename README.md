# Vinttem API

## To run using Makefile:

```
make run
```

## Setup Database Migrations:

To execute migrations:
```
docker-compose exec api alembic upgrade head
```
or:

```
make migrate
```


To create a new migration file:
```
python -m alembic revision --autogenerate -m "Some Contextual Message Overhere"
```

## Tests
```
make tests
```

## Usefull tips:

Docs at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)


To insert a transaction:
```
curl -X POST http:/127.0.0.1:8000/api/v1/transactions/ -H 'Content-Type: application/json' -d '{"user": "Matheus", "value":6.66, "category": 1, "type": 1, "description": "some description"}'
```
