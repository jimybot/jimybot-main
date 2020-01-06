import enum
from sqlalchemy import Boolean, String, Column, Enum
from sqlalchemy.sql import expression
from sqlalchemy_api_handler import ApiHandler

from models.utils.db import Model

class FeatureToggle(enum.Enum):
    WEBAPP = "La webapp est activée"


class Feature(ApiHandler,
              Model):

    description = Column(String(300), nullable=False)
    isActive = Column(Boolean,
                      nullable=False,
                      server_default=expression.true(),
                      default=True)
    name = Column(Enum(FeatureToggle), unique=True, nullable=False)

    @property
    def nameKey(self):
        return str(self.name).replace('FeatureToggle.', '')
