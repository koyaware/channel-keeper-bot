"""'initial'

Revision ID: 8eee89991005
Revises: 
Create Date: 2023-02-23 10:04:13.745922

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8eee89991005'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('another_channel',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('channels',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('tg_post', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('users',
    sa.Column('tg_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('tg_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('channels')
    op.drop_table('another_channel')
    # ### end Alembic commands ###
