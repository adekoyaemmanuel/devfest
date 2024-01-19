"""empty message

Revision ID: 458afa86ab4a
Revises: 
Create Date: 2024-01-11 10:34:17.332929

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '458afa86ab4a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('admin_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('admin_username', sa.String(length=20), nullable=True),
    sa.Column('admin_pwd', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('admin_id')
    )
    op.create_table('level',
    sa.Column('level_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('level_name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('level_id')
    )
    op.create_table('state',
    sa.Column('state_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('state_name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('state_id')
    )
    op.create_table('lga',
    sa.Column('lga_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('lga_name', sa.String(length=100), nullable=False),
    sa.Column('lga_stateid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['lga_stateid'], ['state.state_id'], ),
    sa.PrimaryKeyConstraint('lga_id')
    )
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_fname', sa.String(length=100), nullable=False),
    sa.Column('user_lname', sa.String(length=100), nullable=False),
    sa.Column('user_email', sa.String(length=120), nullable=False),
    sa.Column('user_password', sa.String(length=120), nullable=True),
    sa.Column('user_phone', sa.String(length=120), nullable=True),
    sa.Column('user_pix', sa.String(length=120), nullable=True),
    sa.Column('user_datereg', sa.DateTime(), nullable=True),
    sa.Column('user_levelid', sa.Integer(), nullable=True),
    sa.Column('user_stateid', sa.Integer(), nullable=True),
    sa.Column('user_lgaid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_levelid'], ['level.level_id'], ),
    sa.ForeignKeyConstraint(['user_lgaid'], ['lga.lga_id'], ),
    sa.ForeignKeyConstraint(['user_stateid'], ['state.state_id'], ),
    sa.PrimaryKeyConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('lga')
    op.drop_table('state')
    op.drop_table('level')
    op.drop_table('admin')
    # ### end Alembic commands ###