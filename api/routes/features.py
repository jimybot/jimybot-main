from flask import current_app as app, jsonify
from sqlalchemy_api_handler import as_dict

from models.feature import Feature
from routes.utils.includes import FEATURE_INCLUDES


@app.route('/features', methods=['GET'])
def list_features():
    features = Feature.query.all()
    return jsonify([as_dict(feature, includes=FEATURE_INCLUDES) for feature in features]), 200
