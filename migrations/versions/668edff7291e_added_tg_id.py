"""'added_tg_id'

Revision ID: 668edff7291e
Revises: 66e460cc994e
Create Date: 2023-02-24 14:36:19.600097

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '668edff7291e'
down_revision = '66e460cc994e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('channels', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'channels', 'users', ['user_id'], ['tg_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'channels', type_='foreignkey')
    op.drop_column('channels', 'user_id')
    # ### end Alembic commands ###
