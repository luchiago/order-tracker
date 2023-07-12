FROM python:3.11-slim-buster

ENV PYTHONUNBUFFERED=1
ENV DISPLAY=:99

WORKDIR /app

RUN apt-get update && apt-get install -y \
    firefox-esr \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y \
    wget \
    && rm -rf /var/lib/apt/lists/*
RUN wget -qO- https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-linux64.tar.gz | tar -xz -C /usr/local/bin

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 4444

CMD ["python", "main.py"]
