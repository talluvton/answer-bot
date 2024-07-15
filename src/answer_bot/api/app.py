from flask import Flask
from flask_smorest import Api
import os 

from answer_bot.resources.question import blp as QuestionBlueprint
from answer_bot.utils.postgresql import db


def create_app():
    app = Flask(__name__)

    app.config["FLASK_ENV"] = os.environ.get("ENVIRONMENT", "localhost")
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Questions REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('POSTGRESQL_CONNECTION_STRING')
    if app.config["FLASK_ENV"] == "localhost":
        app.config["SQLALCHEMY_DATABASE_URI"] = app.config["SQLALCHEMY_DATABASE_URI"].replace("db", "localhost")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    api = Api(app)

    api.register_blueprint(QuestionBlueprint)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8000)
