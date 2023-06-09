"""Initial migration

Revision ID: c7f346f338fb
Revises: 
Create Date: 2023-05-23 23:14:33.055100

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7f346f338fb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('actor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('imdb_id', sa.String(length=20), nullable=True),
    sa.Column('wiki_id', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('imdb_id'),
    sa.UniqueConstraint('wiki_id')
    )
    op.create_table('director',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('imdb_id', sa.String(length=20), nullable=True),
    sa.Column('wiki_id', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('imdb_id'),
    sa.UniqueConstraint('wiki_id')
    )
    op.create_table('genre',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('imdb_id', sa.String(length=20), nullable=True),
    sa.Column('wiki_id', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('imdb_id'),
    sa.UniqueConstraint('wiki_id')
    )
    op.create_table('movie',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('pubdate', sa.Date(), nullable=True),
    sa.Column('wiki_id', sa.String(length=20), nullable=True),
    sa.Column('imdb_id', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('imdb_id'),
    sa.UniqueConstraint('wiki_id')
    )
    op.create_table('movie_actor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.Column('actor_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['actor_id'], ['actor.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('movie_director',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.Column('director_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['director_id'], ['director.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('movie_genre',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.Column('genre_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['genre_id'], ['genre.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movie_genre')
    op.drop_table('movie_director')
    op.drop_table('movie_actor')
    op.drop_table('movie')
    op.drop_table('genre')
    op.drop_table('director')
    op.drop_table('actor')
    # ### end Alembic commands ###
