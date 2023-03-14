from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class OrdenCompra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(50))
    direccion = db.Column(db.String(50))
    producto = db.Column(db.String(50))
    precio = db.Column(db.Numeric)
    cantidad = db.Column(db.Numeric)
    
class OrdenCompraSchema(SQLAlchemyAutoSchema):
    class Meta:
         model = OrdenCompra
         include_relationships = True
         load_instance = True
         
    cliente = fields.String()
    direccion = fields.String()
    producto = fields.String()
    precio = fields.Float()
    cantidad = fields.Float()
