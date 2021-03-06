"""empty message

Revision ID: 09a34ed90fb0
Revises: 5d2187b5e68e
Create Date: 2021-09-15 15:19:04.056932

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09a34ed90fb0'
down_revision = '5d2187b5e68e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
