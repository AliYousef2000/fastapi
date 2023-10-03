"""empty message

Revision ID: e9d52c491b0b
Revises: d66c7b927b0f
Create Date: 2023-10-02 17:18:02.558928

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e9d52c491b0b'
down_revision: Union[str, None] = 'd66c7b927b0f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
