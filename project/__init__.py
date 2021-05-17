import os
from flask import Flask, jsonify
import logging
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from sentry_sdk.integrations.logging import LoggingIntegration
from flask_parameter_validation import ValidateParameters, Json
from project.algorithms import factorial, fibonacci, ackermann

# from project.algorithms import factorial
sentry_logging = LoggingIntegration(
    level=logging.INFO,        # Capture info and above as breadcrumbs
    event_level=logging.ERROR  # Send errors as events
)

sentry_sdk.init(
    dsn="https://1cedb6b067804effb7da7f2ff9216ccc@o679964.ingest.sentry.io/5770308",
    integrations=[FlaskIntegration(), sentry_logging],
    traces_sample_rate=1.0,
)

app = Flask(__name__)

# set Config
app_settings=os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)


# Endpoints
@app.route('/factorial', methods=['GET'])
@ValidateParameters()
def factorialController(number: int = Json(min_int=0),):
  return jsonify({
    'status': 'success',
    'message': str(factorial(number)),
  })

@app.route('/fibonacci', methods=['GET'])
@ValidateParameters()
def fibonacciController(number: int = Json(min_int=0),):
  return jsonify({
    'status': 'success',
    'message': str(fibonacci(number)),
  })

@app.route('/ackermann', methods=['GET'])
@ValidateParameters()
def ackermannController(
  row: int = Json(min_int=0), 
  column: int = Json(min_int=0)
  ):
  return jsonify({
    'status': 'success',
    'message': str(ackermann(row,column)),
  })