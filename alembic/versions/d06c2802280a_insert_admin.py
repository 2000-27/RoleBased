"""insert admin

Revision ID: d06c2802280a
Revises: c03a9776da91
Create Date: 2023-09-21 14:09:48.976474

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd06c2802280a'
down_revision: Union[str, None] = 'c03a9776da91'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer

def upgrade() -> None:
    accounts_table = table(
        "user",
        column("id", Integer),
        column("email", String),
        column("password", String),
        column('role_id',Integer),
        column("username", String),
        
      )
    
    op.bulk_insert(
        accounts_table,
        [
            {
               "id": 1,
                "email":"admin@gmail.com",
                "password":"34323",
                "role_id": 1,
                "username":"NEETU",
            },
        ],
    )


def downgrade() -> None:
    pass
