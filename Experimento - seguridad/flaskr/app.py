from flaskr import create_app
from flask_restful import Api
from .vistas import VistaOrden, vistaAutorizador
from flask_cors import CORS
from flask_jwt_extended import JWTManager

app = create_app('default')
app_context = app.app_context()
app_context.push()
cors = CORS(app)

api = Api(app)
api.add_resource(VistaOrden, '/ordenes')
api.add_resource(vistaAutorizador, '/autorizador')
jwt = JWTManager(app)
