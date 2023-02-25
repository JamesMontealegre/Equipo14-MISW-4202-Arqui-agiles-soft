from flask_restful import Resource
from ..tareas import obtener_rutas, registrar_log
from flask import jsonify,request
from datetime import datetime

class VistaRuta(Resource):

     def get(self, microservicio):
        # registrar_log.delay('obtener rutas en {}'.format(microservicio), datetime.utcnow())
         result = obtener_rutas.delay(microservicio)
         rutas = result.get()
         return jsonify(rutas)      

class VistaLog(Resource):
    def post(self):
        print(request.json["mensaje"])
        registrar_log.delay(request.json["mensaje"],datetime.utcnow())
        return "ok", 200 
