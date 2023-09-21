"""add column username

Revision ID: 8c754f309799
Revises: f1005c8c8dec
Create Date: 2023-09-21 14:05:51.845155

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8c754f309799'
down_revision: Union[str, None] = 'f1005c8c8dec'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
   with op.batch_alter_table("user") as alter_table_users_op:
        alter_table_users_op.add_column(
          sa.Column("username", sa.String()))


def downgrade() -> None:
   op.drop_table('user')
   op.drop_table('role')
   
