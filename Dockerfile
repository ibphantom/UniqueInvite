# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for the Flask app
EXPOSE 5000

# Define environment variables for MySQL connection
# These can be overridden in Docker run or Docker Compose
ENV MYSQL_HOST=mariadb
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=your_password
ENV MYSQL_DATABASE=your_database

# Run the Flask app
CMD ["python", "app.py"]
