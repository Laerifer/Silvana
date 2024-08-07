# Usa una imagen base de Python
FROM python:3.8-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia todos los archivos y carpetas al contenedor
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que tu servidor escucha
EXPOSE 8080

# Ejecuta el archivo server.py
CMD ["python3", "server.py"]
