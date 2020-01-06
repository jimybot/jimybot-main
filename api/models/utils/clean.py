from postgresql_audit.flask import versioning_manager
from sqlalchemy_api_handler import logger

from models.utils.db import db
from models.user import User

def clean_all_database():
    """ Order of deletions matters because of foreign key constraints """
    logger.info("clean all the database...")
    User.query.delete()
    versioning_manager.activity_cls.query.delete()
    db.session.commit()
    logger.info("clean all the database...Done.")
