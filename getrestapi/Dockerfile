# Use the official Python image as the base image
FROM python:3.8-slim
ENV FLASK_APP flaskapi.py
# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /getapi
COPY flaskapi.py /app
COPY team.json /app

# Install Flask and any other dependencies
RUN pip install Flask

# Expose port 5000 for the Flask app
EXPOSE 5000

# Run the Flask app when the container launches
CMD ["flask", "run", "--host", "0.0.0.0"]
