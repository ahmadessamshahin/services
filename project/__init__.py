import os
from flask import Flask, jsonify

app = Flask(__name__)

# set Config
app_settings=os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

@app.route('/users/ping', methods=['GET'])
def ping_pong():
  return jsonify({
    'status': 'successll',
    'message': 'pongsss5!'
  })