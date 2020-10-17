"""
resources/dog.py.
Authors: Oscar Espirilla
"""
import logging
import requests
from flask_restful import Resource


class DogListResource(Resource):
    """List 3 random dogs from dog.ceo"""

    def get(self):
        """Get method"""
        try:
            dog_list = requests.get("https://dog.ceo/api/breeds/image/random/3")
            data = dog_list.json()
            if not data:
                return {
                           'message': 'Dog List not found',
                           'status': 'error'
                       }, 404

            return {
                'data': data,
            }
        except Exception as ex:
            logging.error('ERROR getting the dog list from API: {0}'.format(ex))
            return {'status': 'error', 'message': str(ex)}, 500


class DogResource(Resource):
    """Get a random dog from dog.ceo."""

    def get(self):
        """Get method"""
        try:
            random_dog = requests.get("https://dog.ceo/api/breeds/image/random")
            data = random_dog.json()

            if not data:
                return {
                           'message': 'Dog not found',
                           'status': 'error'
                       }, 404

            return {
                'data': data,
            }
        except Exception as ex:
            logging.error('ERROR getting the random dog from api: {0}'.format(ex))
            return {'status': 'error', 'message': str(ex)}, 500
