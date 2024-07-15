import openai
import os
from flask_smorest import abort

from answer_bot.utils.postgresql import insert_q_to_db
from answer_bot.models.question import QuestionModel


class OpenAIClient():
    _client = openai.OpenAI(api_key=os.getenv("API_KEY"))
    _chat_log = []


    @classmethod
    def ask_question(cls, q: str) -> QuestionModel:
        "Send a question to ChatGPT - retrieves answer"
        # append to session's chat_log
        cls._chat_log.append({"role": "user", "content": q})
        try:
            # send the question
            response = cls._client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=cls._chat_log
            )
            # extract response
            assistant_response = response.choices[0].message.content
            question_record = QuestionModel(question=q, answer=assistant_response)
            insert_q_to_db(question_record)
            return question_record
        except Exception as err:
            abort(500, message=f"An unexpected error occurred: {str(err)}")