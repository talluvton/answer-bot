# Use the official Python 3.11 image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

ENV ENVIRONMENT development
ENV PYTHONPATH "./src"
ENV FLASK_APP "src/answer_bot/api/app.py"
# Expose the port the app runs on
EXPOSE 8000

# Define the command to run the application
CMD ["python", "src/answer_bot/api/app.py", "--host=0.0.0.0", "--port=8000"]
