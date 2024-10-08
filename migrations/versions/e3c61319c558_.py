"""empty message

Revision ID: e3c61319c558
Revises: 53c69f53c282
Create Date: 2024-08-12 10:32:07.434789

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3c61319c558'
down_revision = '53c69f53c282'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blog_post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('title', sa.String(length=140), nullable=True),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('summary', sa.String(length=140), nullable=True),
    sa.Column('thumbnail', sa.String(length=140), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blog_post')
    # ### end Alembic commands ###
