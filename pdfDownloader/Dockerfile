# Use Python + Playwright base image
FROM mcr.microsoft.com/playwright/python:v1.41.2-focal

# Set working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Expose port (Render will override)
EXPOSE 5000

# Run Flask app
CMD ["python", "server.py"]
