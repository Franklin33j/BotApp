# Utilizar una imagen base de Python
FROM python:3.11

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el código fuente de tu aplicación al contenedor
COPY . .

# Instalar las dependencias de tu aplicación
RUN pip install python-telegram-bot

# Exponer el puerto en el que tu aplicación estará escuchando
EXPOSE 8080

# Comando para ejecutar tu aplicación cuando se inicie el contenedor
CMD ["python", "index.py"]
