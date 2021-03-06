"""create tasks table

Revision ID: 8afbd4758e80
Revises:
Create Date: 2019-05-29 12:21:02.469552

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8afbd4758e80'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tasks',
        sa.Column('id', sa.String(length=256), nullable=False),
        sa.Column('started_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('func_name', sa.String(length=256), nullable=False),
        sa.Column('status', sa.String(length=256), nullable=False),
        sa.Column('enqueued_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('ended_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('result', sa.String(length=1024), nullable=True),
        sa.Column('duration', sa.Numeric(precision=18, scale=6), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tasks')
    # ### end Alembic commands ###
