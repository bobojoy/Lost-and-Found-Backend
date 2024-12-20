"""updated seed

Revision ID: 551ecd10a804
Revises: 
Create Date: 2024-11-25 10:39:00.639925

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '551ecd10a804'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('_password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('rewards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('points', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('_password_hash', sa.String(length=128), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('founditems',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=True),
    sa.Column('reward', sa.Integer(), nullable=True),
    sa.Column('place_lost', sa.String(length=100), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lostitems',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=True),
    sa.Column('reward', sa.Integer(), nullable=True),
    sa.Column('place_lost', sa.String(length=100), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('approved_by_id', sa.Integer(), nullable=True),
    sa.Column('image_url', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['approved_by_id'], ['admins.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reward_payments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('reward_id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('date_paid', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['reward_id'], ['rewards.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('claims',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('founditem_id', sa.Integer(), nullable=False),
    sa.Column('lostitem_id', sa.Integer(), nullable=True),
    sa.Column('is_approved', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['founditem_id'], ['founditems.id'], ),
    sa.ForeignKeyConstraint(['lostitem_id'], ['lostitems.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('lost_item_id', sa.Integer(), nullable=True),
    sa.Column('found_item_id', sa.Integer(), nullable=True),
    sa.Column('content', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['found_item_id'], ['founditems.id'], ),
    sa.ForeignKeyConstraint(['lost_item_id'], ['lostitems.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    op.drop_table('claims')
    op.drop_table('reward_payments')
    op.drop_table('lostitems')
    op.drop_table('founditems')
    op.drop_table('users')
    op.drop_table('rewards')
    op.drop_table('admins')
    # ### end Alembic commands ###
