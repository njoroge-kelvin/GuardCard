FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /code

# System deps needed to build/run asyncpg, bcrypt, cryptography, etc.
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential libpq-dev curl \
    && rm -rf /var/lib/apt/lists/*

# Install deps (requires package sources) so this layer is cached unless pyproject.toml changes
COPY pyproject.toml ./
COPY app ./app
RUN pip install --upgrade pip && pip install .

# Now copy the rest of the source
COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]