# Use a base image with Python installed
FROM python:3.8-slim

# Create a directory for your application
WORKDIR /app

# Copy your server scripts into the container
COPY serviceprovider.py .
COPY serviceprovider1.py .
COPY config_file.json /app

# Install any dependencies your servers might have
# For this example, there are no additional dependencies

# Expose the ports your servers will listen on
EXPOSE 8080
EXPOSE 8081

# Start your servers when the container is run
CMD [ "python", "serviceprovider.py" ]
CMD [ "python", "serviceprovider1.py" ]
