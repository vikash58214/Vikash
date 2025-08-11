# Use Python 3.10 + Playwright base image
FROM mcr.microsoft.com/playwright/python:v1.41.2-jammy

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install chromium for playwright
RUN playwright install --with-deps chromium

COPY . .

EXPOSE 5000

CMD ["python", "server.py"]
