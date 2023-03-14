from flask_restful import Resource
import requests
from flask import request
from ..modelos import db, OrdenCompra, OrdenCompraSchema

orden_compra_schema = OrdenCompraSchema()

class VistaOrdenCompra(Resource):

    def get(self):
        return 'Test Orden Compra OK'

    def post(self):
        cliente = request.json["cliente"]
        direccion = request.json["direccion"]
        producto = request.json["producto"]
        precio = request.json["precio"]
        cantidad = request.json["cantidad"]
        ordenCompra = OrdenCompra(
            cliente=cliente,
            direccion=direccion,
            producto=producto,
            precio=precio,
            cantidad=cantidad
        )
        db.session.add(ordenCompra)
        db.session.commit()
        return orden_compra_schema.dump(ordenCompra)
