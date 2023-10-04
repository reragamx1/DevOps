FROM python:3.8-slim
ENV FLASK_APP restapi_curd_operations.py
# Set the working directory in the container
WORKDIR /script

# Copy the current directory contents into the container at /getapi
COPY restapi_curd_operations.py /script

# Install Flask and any other dependencies
RUN pip install Flask

# Expose port 5000 for the Flask app
EXPOSE 5000

# Run the Flask app when the container launches
CMD ["flask", "run", "--host", "0.0.0.0"]
