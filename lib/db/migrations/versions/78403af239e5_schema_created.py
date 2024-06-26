"""schema created

Revision ID: 78403af239e5
Revises: 
Create Date: 2024-03-24 19:01:03.703496

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '78403af239e5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('assets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('issuer_name', sa.String(), nullable=True),
    sa.Column('current_price', sa.Float(), nullable=True),
    sa.Column('maturity_date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('clients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('account_type', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_number', sa.String(), nullable=True),
    sa.Column('account_balance', sa.Float(), nullable=True),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['clients.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('holdings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=True),
    sa.Column('asset_id', sa.Integer(), nullable=True),
    sa.Column('number_of_shares', sa.Float(), nullable=True),
    sa.Column('purchase_price', sa.Float(), nullable=True),
    sa.Column('purchase_date', sa.Date(), nullable=True),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['account_id'], ['profile.id'], ),
    sa.ForeignKeyConstraint(['asset_id'], ['assets.id'], ),
    sa.ForeignKeyConstraint(['client_id'], ['clients.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('holdings')
    op.drop_table('profile')
    op.drop_table('clients')
    op.drop_table('assets')
    # ### end Alembic commands ###
