import pytest
from flask.testing import FlaskClient
from unittest.mock import patch
from typing import Generator

from answer_bot.api.app import create_app 

@pytest.fixture
def client() -> Generator[FlaskClient, None, None]:
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@patch('answer_bot.clients.openai.OpenAIClient.ask_question')
def test_ask_question(mock_ask_question, client):
    mock_ask_question.return_value = {
        "question": "What is the capital of Israel?",
        "answer": "Jerusalem"
    }

    response = client.post('/ask', json={
        "question": "What is the capital of Israel?"
    })

    assert response.status_code == 201
    data = response.get_json()
    assert data['answer'] == "Jerusalem"


@patch('answer_bot.clients.openai.OpenAIClient.ask_question')
def test_ask_question_not_valid_input(mock_ask_question, client):
    mock_ask_question.return_value = {
        "question": 123
    }

    response = client.post('/ask', json={
        "question": 123
    })

    assert response.status_code == 422

   