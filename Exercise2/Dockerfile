# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script to the container
COPY Exercise2/serviceprovider.py /app
COPY Exercise2/config_file.json /app

# Run the Python script when the container launches
ENTRYPOINT ["python", "serviceprovider.py"]
