from flask.views import MethodView
from flask_smorest import Blueprint 
from answer_bot.schemas.question import QuestionSchema
from answer_bot.models.question import QuestionModel
from answer_bot.clients.openai import OpenAIClient


blp = Blueprint("Questions", __name__, description="Operaions on questions")


@blp.route("/question/<uuid:question_id>")
class Question(MethodView):
    @blp.response(200, QuestionSchema)
    def get(self, question_id):
        question = QuestionModel.query.get_or_404(question_id)
        return question


@blp.route("/questions")
class QuestionsList(MethodView):
    @blp.response(200, QuestionSchema(many=True))
    def get(self):
        return QuestionModel.query.all()

@blp.route("/ask")
class AskQuestion(MethodView):
    @blp.arguments(QuestionSchema)
    @blp.response(201, QuestionSchema)
    def post(self, question_data):
        question_content = question_data["question"]
        answer = OpenAIClient.ask_question(question_content)
        return answer
        