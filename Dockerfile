# Use Python 3.10 + Playwright base image
FROM mcr.microsoft.com/playwright/python:v1.41.2-jammy

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "server:app"]
