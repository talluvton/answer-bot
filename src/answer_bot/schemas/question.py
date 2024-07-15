from marshmallow import Schema, fields, post_load

class QuestionSchema(Schema):
    question_id = fields.UUID(dump_only=True)
    question = fields.Str(required=True)
    answer = fields.Str(dump_only=True)
    update_date = fields.DateTime(dump_only=True)