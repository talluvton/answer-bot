from answer_bot.utils.postgresql import db 
import uuid
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime


class QuestionModel(db.Model):
    __tablename__ = "questions"
    question_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    question = db.Column(db.String, nullable=False)
    answer = db.Column(db.String, nullable=True)
    update_date = db.Column("update_date", db.DateTime, nullable=False, default=datetime.now)