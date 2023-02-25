# Equipo14-MISW-4202-Arqui-agiles-soft

Repositorio código fuente de experimentos el cual contiene dos carpetas uno para el Sincrono y otra para el Asincrono.

# Instalacion: 

Para cada uno de los proyectos sincrono y asincrono se debe: 
1. Crear los entornos virtuales. =>  Comando : **"python3 -m venv venv"**
2. Activar los entornos viruales. => Comando : **".\venv\Scripts\activate"**
3. Instalar los requerimientos para cada proyecto : Comando **"pip install -r requirements.txt"**
4. Iniciar cada uno de los servicios en el puertos así, segun experimento:
5.    Api_Gateway: Comando **"flask run -p 5001"** (Carpeta Flaskr) (Experimento Sincrono - Asincrono)
6.    Microservicio_1: Comando **"flask run -p 5002"** (Carpeta microservicio_1) (Unicamente en Experimento Asincrono)
7.    Microservicio_1: Comando Iniciar componente colas **"celery -A tareas worker -l info"** (Carpeta microservicio_1) (Unicamente en Experimento Asincrono)
8.    Microservicio_2: Comando **"flask run -p 5003"** (Carpeta microservicio_2) (Experimento Sincrono - Asincrono)
9.    Microservicio_2: Comando **"flask run -p 5004"** (Carpeta microservicio_2) (Experimento Sincrono - Asincrono)
10.   Microservicio_2: Comando **"flask run -p 5005"** (Carpeta microservicio_2) (Experimento Sincrono - Asincrono)

Con estos pasos quedan listos e iniciados los componentes de acuerdo al experimento que se desee realizar.
