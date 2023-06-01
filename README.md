# Vinttem API

### To run using Makefile:

```
make run
```

### Setup Database Migrations:

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
