# Use Playwright base image
FROM mcr.microsoft.com/playwright/python:v1.41.2-focal

WORKDIR /app

# Copy only requirements first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose port
EXPOSE 5000

# Run with Gunicorn for production
CMD ["gunicorn", "-b", "0.0.0.0:5000", "server:app"]
