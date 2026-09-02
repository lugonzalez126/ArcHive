"""add role to users

Revision ID: 9f3b7c1a2d4e
Revises: 1c06d05e4690
Create Date: 2026-09-02 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9f3b7c1a2d4e'
down_revision: Union[str, Sequence[str], None] = '1c06d05e4690'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'users',
        sa.Column('role', sa.String(length=20), nullable=False, server_default='student')
    )


def downgrade() -> None:
    op.drop_column('users', 'role')
