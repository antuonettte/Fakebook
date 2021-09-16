"""empty message

Revision ID: c3f606720f04
Revises: e886b40f00a4
Create Date: 2021-09-15 15:22:32.016102

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3f606720f04'
down_revision = 'e886b40f00a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'last_name')
    op.drop_column('post', 'first_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('first_name', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    op.add_column('post', sa.Column('last_name', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
