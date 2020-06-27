"""empty message

Revision ID: 80f6bf97516a
Revises: 4eb055a911b5
Create Date: 2020-06-26 13:47:29.535635

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80f6bf97516a'
down_revision = '4eb055a911b5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
