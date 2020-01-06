def import_models():
    from models.feature import Feature
    from models.user import User
    return list(locals().values())
