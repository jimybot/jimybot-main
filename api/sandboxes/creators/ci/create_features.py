from sqlalchemy_api_handler import ApiHandler, logger

from models.feature import Feature, FeatureToggle

def create_features():
    logger.info('   create_features...')

    features_by_name = {}

    for toggle in FeatureToggle:
        feature = Feature(
            description=toggle.value,
            isActive=True,
            name=toggle
        )
        features_by_name['{}'.format(toggle)] = feature

    ApiHandler.save(*features_by_name.values())

    logger.info('   created {} features'.format(len(features_by_name)))

    return features_by_name
