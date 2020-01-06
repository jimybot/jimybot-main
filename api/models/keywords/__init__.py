from sqlalchemy import Index, TEXT
from sqlalchemy.sql.expression import cast
from sqlalchemy.sql.functions import coalesce

from domain.keywords import create_tsvector
from models.user import User

def import_keywords():
    User.__ts_vector__ = create_tsvector(
        cast(coalesce(User.email, ''), TEXT),
        cast(coalesce(User.firstName, ''), TEXT),
        cast(coalesce(User.lastName, ''), TEXT),
    )
    User.__table_args__ = (
        Index(
            'idx_event_fts',
            User.__ts_vector__,
            postgresql_using='gin'
        ),
    )
