# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the entire project into the container's "/app" directory
COPY . /app

# Install the dependencies from requirements.txt in the root
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for Flask
EXPOSE 5000

# Environment variables for database connection
ENV MYSQL_HOST=mariadb
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=your_password
ENV MYSQL_DATABASE=your_database

# Run the Flask app
CMD ["python", "app/app.py"]
