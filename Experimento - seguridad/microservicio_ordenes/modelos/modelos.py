from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class OrdenCompra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(50))
    direccion = db.Column(db.String(50))
    producto = db.Column(db.String(50))
    precio = db.Column(db.Number)
    cantidad = db.Column(db.Number)
    
class OrdenCompraSchema(SQLAlchemyAutoSchema):
    class Meta:
         model = OrdenCompra
         include_relationships = True
         load_instance = True