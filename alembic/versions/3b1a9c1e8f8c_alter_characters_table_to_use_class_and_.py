"""Alter characters table to use class and race IDs

Revision ID: 3b1a9c1e8f8c
Revises: 014fc6a64462
Create Date: 2025-03-24 13:09:01.900076

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import create_engine, MetaData, text


# revision identifiers, used by Alembic.
revision: str = '3b1a9c1e8f8c'
down_revision: Union[str, None] = '014fc6a64462'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Criar uma nova tabela com a estrutura desejada
    op.create_table(
        'characters_new',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('race_id', sa.Integer, sa.ForeignKey('races.id'), nullable=False),
        sa.Column('class_id', sa.Integer, sa.ForeignKey('character_classes.id'), nullable=False),
        sa.Column('level', sa.Integer, nullable=False),
        sa.Column('background', sa.String, nullable=True),
        sa.Column('personality_traits', sa.String, nullable=True)  # Ajuste conforme necessário
    )

    # Copiar dados da tabela antiga para a nova tabela
    conn = op.get_bind()
    conn.execute(
        text('INSERT INTO characters_new (id, name, race_id, class_id, level, background, personality_traits) '
             'SELECT id, name, (SELECT id FROM races WHERE name = race), (SELECT id FROM character_classes WHERE name = character_class), level, background, personality_traits FROM characters')
    )

    # Excluir a tabela antiga
    op.drop_table('characters')

    # Renomear a nova tabela para o nome da tabela original
    op.rename_table('characters_new', 'characters')


def downgrade() -> None:
    """Downgrade schema."""
    # Reverter as alterações (opcional, dependendo da sua necessidade)
    op.create_table(
        'characters_old',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('race', sa.Enum('HUMAN', 'ELF', 'DWARF', 'HALFLING', 'DRAGONBORN', 'TIEFLING', 'HALF_ORC', name='race_enum'), nullable=False),
        sa.Column('character_class', sa.Enum('WARRIOR', 'MAGE', 'CLERIC', 'ROGUE', 'PALADIN', 'RANGER', 'BARD', name='class_enum'), nullable=False),
        sa.Column('level', sa.Integer, nullable=False),
        sa.Column('background', sa.String, nullable=True),
        sa.Column('personality_traits', sa.String, nullable=True)  # Ajuste conforme necessário
    )

    # Copiar dados da tabela nova para a tabela antiga
    conn = op.get_bind()
    conn.execute(
        text('INSERT INTO characters_old (id, name, race, character_class, level, background, personality_traits) '
             'SELECT id, name, (SELECT name FROM races WHERE id = race_id), (SELECT name FROM character_classes WHERE id = class_id), level, background, personality_traits FROM characters')
    )

    # Excluir a tabela nova
    op.drop_table('characters')

    # Renomear a tabela antiga para o nome da tabela original
    op.rename_table('characters_old', 'characters')
