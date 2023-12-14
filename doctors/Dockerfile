# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the application file into the container at /usr/src/app
COPY app.py .

# Install Flask
RUN pip install Flask

# Make port 7071 available to the world outside this container
EXPOSE 9090

# Run app.py when the container launches
CMD ["python", "app.py"]

# Updated