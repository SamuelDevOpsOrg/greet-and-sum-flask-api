# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the environment variable for Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=production 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install system dependencies
RUN apt-get update && \
    apt-get install -y build-essential gcc dialog openssh-server && \
    rm -rf /var/lib/apt/lists/*

# Set the root password for SSH
RUN echo "root:Docker!" | chpasswd

COPY sshd_config /etc/ssh/

# Copy entrypoint.sh into the container and make it executable
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Install the dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt pytest

# Copy the rest of the application code into the container
COPY . .

# Run tests to verify the app works correctly
RUN pytest --disable-warnings

EXPOSE 5000 2222

# Run the application using a production-ready server
# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
ENTRYPOINT ["/entrypoint.sh"]