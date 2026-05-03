import docker
import datetime


def guardar_log(mensaje):
    with open("log.txt", "a") as f:
        fecha = datetime.datetime.now()
        f.write(f"{fecha} - {mensaje}\n")


cliente = docker.from_env()
contenedor = "pruebadocker"

try:
    c = cliente.containers.get(contenedor)
    if c.status == "running":
        guardar_log(f"{contenedor} está corriendo OK")
    else:
        guardar_log(f"ALERTA: {contenedor} no está corriendo")
except docker.errors.NotFound:
    guardar_log(f"ALERTA: {contenedor} no existe")
