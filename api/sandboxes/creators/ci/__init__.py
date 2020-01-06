from sqlalchemy_api_handler import logger

from sandboxes.creators.ci.create_features import create_features
from sandboxes.creators.ci.create_users import create_users

def create_sandbox():
    logger.info('create_ci_sandbox...')

    create_features()

    create_users()

    logger.info('create_ci_sandbox...Done.')
