"""'added_memes'

Revision ID: f5601a54f628
Revises: 8eee89991005
Create Date: 2023-02-24 11:06:37.188935

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5601a54f628'
down_revision = '8eee89991005'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('memes',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('Id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('memes')
    # ### end Alembic commands ###
