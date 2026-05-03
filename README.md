# Monitor Docker

Script en Python que monitorea si un contenedor Docker está corriendo y registra alertas en un log.

## ¿Qué hace?

- Verifica el estado del contenedor `pruebadocker`
- Guarda un log con fecha y hora de cada verificación
- En producción corre en loop cada 60 segundos

## Tecnologías

- Python
- Docker
- GitHub Actions (CI)

## Uso

```bash
python monitor.py
```
