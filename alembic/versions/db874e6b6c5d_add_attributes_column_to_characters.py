"""Add attributes column to characters

Revision ID: db874e6b6c5d
Revises: 3b1a9c1e8f8c
Create Date: 2025-03-24 19:01:58.917125

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'db874e6b6c5d'
down_revision: Union[str, None] = '3b1a9c1e8f8c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('characters', sa.Column('attributes', sa.JSON(), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('characters', 'attributes')
