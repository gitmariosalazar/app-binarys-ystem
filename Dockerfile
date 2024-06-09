# Usa una imagen base existente
FROM python:3.11.5

# Establece el directorio de trabajo en /app
WORKDIR /src

# Copia el archivo actual (en el mismo directorio que el Dockerfile) al directorio de trabajo en la imagen
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Expone el puerto 80 para que las comunicaciones externas puedan acceder a él
EXPOSE 5000

# Ejecuta la aplicación cuando se inicie el contenedor
CMD ["python", "src/app.py"]
