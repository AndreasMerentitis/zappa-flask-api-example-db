"""posts table

Revision ID: 0089fec63174
Revises: 116fb9b6b289
Create Date: 2019-04-21 15:55:50.676311

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0089fec63174'
down_revision = '116fb9b6b289'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('body', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_created_at'), 'post', ['created_at'], unique=False)
    op.create_index(op.f('ix_post_updated_at'), 'post', ['updated_at'], unique=False)
    op.add_column('user', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_user_created_at'), 'user', ['created_at'], unique=False)
    op.create_index(op.f('ix_user_updated_at'), 'user', ['updated_at'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_updated_at'), table_name='user')
    op.drop_index(op.f('ix_user_created_at'), table_name='user')
    op.drop_column('user', 'updated_at')
    op.drop_column('user', 'created_at')
    op.drop_index(op.f('ix_post_updated_at'), table_name='post')
    op.drop_index(op.f('ix_post_created_at'), table_name='post')
    op.drop_table('post')
    # ### end Alembic commands ###
