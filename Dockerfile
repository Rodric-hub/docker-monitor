FROM python:3.13
COPY . /app
WORKDIR /app
CMD ["python", "monitor.py"]