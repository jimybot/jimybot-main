from sqlalchemy_api_handler import ApiHandler, as_dict, humanize

from models.user import User
from routes.utils.includes import USER_INCLUDES
from utils.credentials import PLAIN_DEFAULT_TESTING_PASSWORD
from tests.utils.clean import with_clean_all_database
from tests.utils.TestClient import TestClient


class Get:
    class Returns200:
        @with_clean_all_database
        def when_default_request(self, app):
            # given
            user_dicts = [
                {
                    "email": "foo@bar.com"
                },
                {
                    "email": "karl@marx.eu"
                }
            ]
            users = list(map(lambda user_dict: User(**user_dict), user_dicts))
            for user in users:
                user.set_password(PLAIN_DEFAULT_TESTING_PASSWORD)
            ApiHandler.save(*users)
            auth_request = TestClient(app.test_client())\
                            .with_auth(email=users[0].email)

            # when
            url = '/users/{}'.format(humanize(users[1].id))
            response = auth_request.get(url)

            # then
            assert response.status_code == 200
            assert set(as_dict(users[1], includes=USER_INCLUDES).items()) \
                    .issubset(set(response.json.items()))
