"""add created at column to player

Revision ID: 0baf223a780d
Revises: 59deb64a53a9
Create Date: 2023-10-02 17:08:23.382020

"""
from typing import Sequence, Union
from sqlalchemy import TIMESTAMP,text
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0baf223a780d'
down_revision: Union[str, None] = '59deb64a53a9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('player',sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=text('now()')))
    pass


def downgrade() -> None:
    op.drop_column('created_at',table_name='player')
    pass
