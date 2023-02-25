import requests
from .config import celery_app

@celery_app.task(name='obtener_rutas')
def obtener_rutas(microservicio):
    rutas = []
    if(microservicio == 'ms1'):
        response = requests.get('http://localhost:5003/rutas')
        rutas = response.json()
    elif(microservicio == 'ms2'):
        response = requests.get('http://localhost:5004/rutas')
        rutas = response.json()
    elif(microservicio == 'ms3'):
        response = requests.get('http://localhost:5005/rutas')
        rutas = response.json()
    else:
        response = requests.get('http://localhost:5003/rutas')
        rutas = response.json()
    return rutas

@celery_app.task(name='registrar_log')
def registrar_log(message, fecha):
    with open('logs.txt', 'a+') as file:
        file.write('Log: {} - {}\n'.format(message, fecha))
