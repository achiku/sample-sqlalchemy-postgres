"""init

Revision ID: e3a1f41048be
Revises:
Create Date: 2016-06-25 19:06:12.960103

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3a1f41048be'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('account',
                    sa.Column('id', sa.BIGINT(), nullable=False),
                    sa.Column('email', sa.TEXT(), nullable=False),
                    sa.Column('phone_number', sa.TEXT(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('item',
                    sa.Column('id', sa.BIGINT(), nullable=False),
                    sa.Column('name', sa.TEXT(), nullable=False),
                    sa.Column('price', sa.Integer(), nullable=True),
                    sa.Column('description', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('sale',
                    sa.Column('id', sa.BIGINT(), nullable=False),
                    sa.Column('account_id', sa.BIGINT(), nullable=False),
                    sa.Column('item_id', sa.BIGINT(), nullable=False),
                    sa.Column('paid_amount', sa.Integer(), nullable=False),
                    sa.Column('sold_at', sa.DateTime(
                        timezone=True), nullable=False),
                    sa.ForeignKeyConstraint(['account_id'], ['account.id'], ),
                    sa.ForeignKeyConstraint(['item_id'], ['item.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade():
    op.drop_table('sale')
    op.drop_table('item')
    op.drop_table('account')
