# Usa una imagen base oficial de Python 3.8 (puedes cambiar a una versión más reciente si lo deseas)
FROM python:3.11.5

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos de requisitos al contenedor de trabajo
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Copia el resto de los archivos de la aplicación al directorio de trabajo del contenedor
COPY api/ .

# Expone el puerto en el que la aplicación se ejecutará (ajusta esto si usas otro puerto)
EXPOSE 5000

# Define el comando para ejecutar la aplicación
CMD ["python", "app.py"]
