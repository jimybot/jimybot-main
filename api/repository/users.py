from sqlalchemy import and_

from domain.keywords import create_filter_matching_all_keywords_in_any_model, \
                            create_get_filter_matching_ts_query_in_any_model
from models.user import User

user_ts_filter = create_get_filter_matching_ts_query_in_any_model(
    User
)

def find_user_by_email(email):
    return User.query.filter_by(email=email).first()

def find_user_by_reset_password_token(token):
    return User.query.filter_by(reset_passwordToken=token).first()

def get_users_join_query(query):
    query = query.outerjoin(UserTag)\
                 .outerjoin(Tag)
    return query

def get_users_query_with_keywords(query, keywords):
    keywords_filter = create_filter_matching_all_keywords_in_any_model(
        user_ts_filter,
        keywords
    )
    query = query.outerjoin(UserTag)\
                 .outerjoin(Tag)\
                 .filter(keywords_filter)
    return query
