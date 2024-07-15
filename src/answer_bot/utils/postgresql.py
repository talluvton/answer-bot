from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def insert_q_to_db(q) -> None:
    db.session.add(q)
    db.session.commit()
