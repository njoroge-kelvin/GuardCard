See below how to setup alembic
```
export DATABASE_URL="postgresql+asyncpg://user:pass@localhost:5432/dbname"
alembic revision --autogenerate -m "init"
alembic upgrade head
```