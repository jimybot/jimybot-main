from flask_login import current_user, login_required
from flask import current_app as app, jsonify, request
from sqlalchemy_api_handler import ApiHandler, \
                                   as_dict, \
                                   listify, \
                                   load_or_404

from models.user import User
from repository.users import get_users_join_query, \
                             get_users_query_with_keywords
from routes.utils.includes import USER_INCLUDES


@app.route('/users/current', methods=['PATCH'])
@login_required
def patch_current_user():
    current_user.populate_from_dict(request.json)
    ApiHandler.save(current_user)
    return jsonify(as_dict(current_user, includes=USER_INCLUDES)), 200
