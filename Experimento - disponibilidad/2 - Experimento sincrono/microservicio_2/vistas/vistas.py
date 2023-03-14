from flask_restful import Resource
from celery import Celery
from ..modelos import Ruta, RutaSchema

ruta_schema = RutaSchema()

class VistaRuta(Resource):

    def get(self):
        return [ruta_schema.dump(ruta) for ruta in Ruta.query.all()]
        