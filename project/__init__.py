import os
from flask import Flask, jsonify, make_response
import logging
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from sentry_sdk.integrations.logging import LoggingIntegration
from flask_parameter_validation import ValidateParameters, Json
from project.algorithms import factorial, fibonacci, ackermann

dsn=os.getenv('DSN')

# from project.algorithms import factorial
sentry_logging = LoggingIntegration(
    level=logging.INFO,        # Capture info and above as breadcrumbs
    event_level=logging.ERROR  # Send errors as events
)
print('DSN: '+dsn)
# logging.info('DSN: '+dsn)
sentry_sdk.init(
    dsn=dsn,
    integrations=[FlaskIntegration(), sentry_logging],
    traces_sample_rate=1.0,
)

app = Flask(__name__)

# set Config
app_settings=os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)


def log_to_sentry(error_message):
  logging.error(error_message)
  return make_response(jsonify({ 
    'status': 'fail',
    'message':  error_message
  }),400)

# Endpoints
@app.route('/factorial', methods=['GET'])
@ValidateParameters(log_to_sentry)
def factorialController(number: int = Json(min_int=0),):
  return jsonify({
    'status': 'success',
    'message': str(factorial(number)),
  })

@app.route('/fibonacci', methods=['GET'])
@ValidateParameters(log_to_sentry)
def fibonacciController(number: int = Json(min_int=0),):
  return jsonify({
    'status': 'success',
    'message': str(fibonacci(number)),
  })

@app.route('/ackermann', methods=['GET'])
@ValidateParameters(log_to_sentry)
def ackermannController(
  row: int = Json(min_int=0), 
  column: int = Json(min_int=0)
  ):
  return jsonify({
    'status': 'success',
    'message': str(ackermann(row,column)),
  })