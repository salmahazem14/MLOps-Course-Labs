FROM python:3.11-slim

WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive  

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["litestar", "--app", "main:app", "run", "--host", "0.0.0.0", "--port", "8000"]