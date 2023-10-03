"""add user table

Revision ID: d66c7b927b0f
Revises: 0baf223a780d
Create Date: 2023-10-02 17:12:02.581879

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd66c7b927b0f'
down_revision: Union[str, None] = '0baf223a780d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('user',
                sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
                sa.Column('email',sa.String(),nullable=False,unique=True),
                sa.Column('password',sa.String(),nullable=False),
                )
    pass


def downgrade() -> None:
    op.drop_table('user')
    pass

