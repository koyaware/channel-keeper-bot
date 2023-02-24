"""'tg_post_deleted'

Revision ID: 041f0bfa88f1
Revises: 7c31b5d36104
Create Date: 2023-02-24 12:12:24.299105

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '041f0bfa88f1'
down_revision = '7c31b5d36104'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('channels', 'tg_post')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('channels', sa.Column('tg_post', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###