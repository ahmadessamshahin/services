from flask.cli import FlaskGroup
import unittest
from project import app

cli = FlaskGroup(app)

@cli.command()
def test():
  """ Run the tests without code coverage"""
  tests =unittest.TestLoader().discover('project/tests', pattern='test*.py')
  result = unittest.TextTestRunner(verbosity=2).run(tests)
  if result.wasSuccessful():
    return 0
  return 1
if __name__ == '__main__':
  cli()
