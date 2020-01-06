from sqlalchemy_api_handler import ApiHandler, logger

from models.user import User
from utils.config import COMMAND_NAME, EMAIL_HOST
from utils.credentials import PLAIN_DEFAULT_TESTING_PASSWORD

USERS_COUNT = 3
default_user = User()
PLAIN_PASSWORD = PLAIN_DEFAULT_TESTING_PASSWORD
default_user.set_password(PLAIN_PASSWORD)
HASHED_PASSWORD = default_user.password

def create_users():
    logger.info('   create_users...')

    users_by_name = {}

    for user_index in range(USERS_COUNT):
        user = User(
            email="{}test.editor{}@{}".format(COMMAND_NAME, user_index, EMAIL_HOST),
            password="{}test.Editor{}".format(COMMAND_NAME, user_index),
            publicName="{} Test Editor {}".format(COMMAND_NAME.upper(), user_index)
        )
        user.password = HASHED_PASSWORD
        users_by_name['{}'.format(user_index)] = user

    ApiHandler.save(*users_by_name.values())

    logger.info('   created {} users'.format(len(users_by_name)))

    return users_by_name
