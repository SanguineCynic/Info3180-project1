"""empty message

Revision ID: 37c65b1a9740
Revises: d7a3ea6db186
Create Date: 2023-03-13 01:34:21.295775

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37c65b1a9740'
down_revision = 'd7a3ea6db186'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('listings', schema=None) as batch_op:
        batch_op.alter_column('title',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.String(length=60),
               nullable=True)
        batch_op.alter_column('num_bedrooms',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('num_bathrooms',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('location',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.String(length=60),
               nullable=True)
        batch_op.alter_column('type',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.String(length=10),
               nullable=True)
        batch_op.alter_column('price',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               type_=sa.Integer(),
               nullable=True)
        batch_op.alter_column('description',
               existing_type=sa.TEXT(),
               nullable=True)
        batch_op.alter_column('image_url',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('listings', schema=None) as batch_op:
        batch_op.alter_column('image_url',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
        batch_op.alter_column('description',
               existing_type=sa.TEXT(),
               nullable=False)
        batch_op.alter_column('price',
               existing_type=sa.Integer(),
               type_=sa.DOUBLE_PRECISION(precision=53),
               nullable=False)
        batch_op.alter_column('type',
               existing_type=sa.String(length=10),
               type_=sa.VARCHAR(length=255),
               nullable=False)
        batch_op.alter_column('location',
               existing_type=sa.String(length=60),
               type_=sa.VARCHAR(length=255),
               nullable=False)
        batch_op.alter_column('num_bathrooms',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('num_bedrooms',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('title',
               existing_type=sa.String(length=60),
               type_=sa.VARCHAR(length=255),
               nullable=False)

    # ### end Alembic commands ###
