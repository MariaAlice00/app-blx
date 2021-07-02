"""Alembic

Revision ID: aa4408c6684d
Revises: 
Create Date: 2021-07-02 16:09:03.729539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa4408c6684d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=True),
    sa.Column('telefone', sa.String(), nullable=True),
    sa.Column('senha', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_usuario_id'), 'usuario', ['id'], unique=False)
    op.create_table('produto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=True),
    sa.Column('detalhes', sa.String(), nullable=True),
    sa.Column('preco', sa.Float(), nullable=True),
    sa.Column('disponivel', sa.Boolean(), nullable=True),
    sa.Column('tamanhos', sa.String(), nullable=True),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], name='fk_usuario'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_produto_id'), 'produto', ['id'], unique=False)
    op.create_table('pedido',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quantidade', sa.Integer(), nullable=True),
    sa.Column('local_entrega', sa.String(), nullable=True),
    sa.Column('tipo_entrega', sa.String(), nullable=True),
    sa.Column('observacao', sa.String(), nullable=True),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.Column('produto_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['produto_id'], ['produto.id'], name='fk_pedido_produto'),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], name='fk_pedido_usuario'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pedido_id'), 'pedido', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_pedido_id'), table_name='pedido')
    op.drop_table('pedido')
    op.drop_index(op.f('ix_produto_id'), table_name='produto')
    op.drop_table('produto')
    op.drop_index(op.f('ix_usuario_id'), table_name='usuario')
    op.drop_table('usuario')
    # ### end Alembic commands ###
