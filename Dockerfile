# Usar Python 3.11
FROM python:3.11-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY requirements.txt .
COPY main.py .
COPY model_medical_insurance.pkl .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer puerto
EXPOSE 8080

# Comando para correr FastAPI con Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
