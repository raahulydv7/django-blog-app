FROM python:3.11-slim

# Prevent .pyc files & enable proper logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBUG=0

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*


# Copy project files
COPY . .


# Copy entrypoint script & make it executable (inside container)
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Create non-root user
RUN adduser --disabled-password --gecos '' appuser
USER appuser

ENTRYPOINT ["/entrypoint.sh"]

# Default command will be overridden by entrypoint
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "blog_project.wsgi:application"]
