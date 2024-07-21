FROM ubuntu:latest
LABEL authors="MIGUEL_MUNOZ"

ENTRYPOINT ["top", "-b"]

# Usar una imagen base oficial de Python
FROM python:3.9

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto
COPY . /app

# Instalar las dependencias
RUN pip install -r requirements.txt

# Exponer el puerto que se usará
EXPOSE 8000

# Comando para ejecutar el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
