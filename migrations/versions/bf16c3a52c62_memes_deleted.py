"""'memes_deleted'

Revision ID: bf16c3a52c62
Revises: f5601a54f628
Create Date: 2023-02-24 11:29:57.823848

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf16c3a52c62'
down_revision = 'f5601a54f628'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('memes')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('memes',
    sa.Column('Id', sa.INTEGER(), server_default=sa.text('nextval(\'"memes_Id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('Id', name='memes_pkey')
    )
    # ### end Alembic commands ###
