# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set the environment variable for Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=production 

# Expose port 5000 for the Flask app
EXPOSE 5000

# # Run the Flask app using python3 -m flask
# CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

# Run the application using a production-ready server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]