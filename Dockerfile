# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed dependencies + update pip
# RUN pip install --upgrade pip

# Make port 8080 available to the world outside this container
EXPOSE 8082

# Define environment variable
ENV NAME Database

# Run the application
CMD ["python", "/app/recap_database.py"]