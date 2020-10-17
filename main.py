"""
app.py
Author: Oscar Espirilla
"""
from flask import Flask
from flask_restful import Api

from resources.dog import DogListResource, DogResource

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)
api = Api(app)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello RJIT from Cloud!'


api.add_resource(DogListResource, '/api/v1/dog/list')
api.add_resource(DogResource, '/api/v1/dog/random')

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
