from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_restful import Resource
import requests
from flask import request, jsonify


class VistaOrden(Resource):
    @jwt_required()
    def get(self):
        return requests.get('http://localhost:5001/ordenes').json()

    @jwt_required()
    def post(self):
        data = request.get_json()
        return requests.post('http://localhost:5001/ordenes', json=data).json()


class vistaAutorizador(Resource):
    def get(self):
        access_token = create_access_token(identity='token')
        return access_token
