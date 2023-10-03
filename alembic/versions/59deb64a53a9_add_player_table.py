"""add player tABLE

Revision ID: 59deb64a53a9
Revises: 
Create Date: 2023-10-02 17:02:38.492219

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '59deb64a53a9'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('player',
                sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
                sa.Column('name',sa.String(),nullable=False),
                sa.Column('team',sa.String(),nullable=False),
                )
    pass


def downgrade() -> None:
    op.drop_table('player')
    pass
