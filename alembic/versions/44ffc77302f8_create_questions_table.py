"""create_questions_table

Revision ID: 44ffc77302f8
Revises: 
Create Date: 2024-07-14 11:53:50.305460

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision: str = '44ffc77302f8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "questions",
        sa.Column("question_id", UUID(as_uuid=True), nullable=False, index=True),
        sa.Column("question", sa.String, nullable=False),
        sa.Column("answer", sa.String, nullable=True),
        sa.Column("update_date", sa.DateTime, server_default=sa.text("(now() at time zone 'UTC')"))
    )


def downgrade() -> None:
    op.drop_table("questions")
