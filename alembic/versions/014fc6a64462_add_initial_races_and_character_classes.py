"""Add initial races and character classes

Revision ID: 014fc6a64462
Revises: 83a79dfdf852
Create Date: 2025-03-23 22:03:03.733485

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine import reflection
from sqlalchemy import Table, MetaData



# revision identifiers, used by Alembic.
revision: str = '014fc6a64462'
down_revision: Union[str, None] = '83a79dfdf852'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Obter a conexão com o banco de dados
    bind = op.get_bind()
    inspector = reflection.Inspector.from_engine(bind)
    
    meta = MetaData()

    # Verificar se a tabela 'races' já existe
    if 'races' not in inspector.get_table_names():
        # Criar tabela de raças
        op.create_table(
            'races',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('name', sa.String, unique=True, nullable=False)
        )

        races = Table('races', meta, autoload_with=op.get_bind())
        # Inserir dados iniciais para raças
        op.bulk_insert(
            races,
            [
                {'name': 'Humano'},
                {'name': 'Elfo'},
                {'name': 'Anão'},
                {'name': 'Halfling'},
                {'name': 'Draconato'},
                {'name': 'Tiefling'},
                {'name': 'Meio-Orc'},
            ]
        )

    # Verificar se a tabela 'character_classes' já existe
    if 'character_classes' not in inspector.get_table_names():
        # Criar tabela de classes de personagem
        op.create_table(
            'character_classes',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('name', sa.String, unique=True, nullable=False)
        )
        
        character_classes = Table('character_classes', meta, autoload_with=op.get_bind())

        # Inserir dados iniciais para classes de personagem
        op.bulk_insert(
            character_classes,
            [
                {'name': 'Guerreiro'},
                {'name': 'Mago'},
                {'name': 'Clérigo'},
                {'name': 'Ladino'},
                {'name': 'Paladino'},
                {'name': 'Patrulheiro'},
                {'name': 'Bardo'},
            ]
        )
    


def downgrade() -> None:
    """Downgrade schema."""
    # Remover as tabelas na reversão da migração
    op.drop_table('races')
    op.drop_table('character_classes')
