from microservicio_2 import create_app
from flask_restful import Api
from .vistas import VistaRuta
from .modelos import db

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaRuta, '/rutas')
