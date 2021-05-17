class BaseConfig:
  """ Base Configuration """
  TESTING = False


class DevelopmentConfig(BaseConfig):
  """ Development Config """
  pass

class TestConfig(BaseConfig):
  """ Test Config """
  TESTING= True

class ProductionConfig(BaseConfig):
  """ ProductionConfig """
  pass