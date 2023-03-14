from flask_restful import Resource
import requests

    
class VistaOrdenCompra(Resource):
    
     def get(self):
       return 'Test Orden Compra OK'