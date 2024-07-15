# ANSWER-BOT

Flask app exposing an API to interact with OpenAI's ChatGPT.
The service returns the answer to the user's question and store it in a database.

# Requirements
- python >= 3.11

# Use Docker Compose to build and run the application:
```bash
docker compose build --no-cache
docker compose up -d 
```

# Access Swagger UI:
http://127.0.0.1:8000/swagger-ui for the API documentation.

# Ask Question route:
http://127.0.0.1:8000/ask
other routes are available to retrieve the questions data - refer to the Swagger documentation for more.

# Testing:
```bash
pytest
```