Project to test at local machine and/or deploy the API on Google Cloud Run

El archivo main.py es un script en python que se encarga de exponer el API para
ejecutar el modelo en linea

• Para probar localmente:

– Ejecutar el comando: python -m uvicorn main:app –reload

– Abrir el archivo medical_prediction _local.html en un browser, este es un

formulario que llama el servicio que se ejecutó en el paso anterior y muestra las
predicciones realiazdas por el model

• Para exportar el modelo en linea:

– El archivo Dockerfile es el encargardo de desplegar los servicios en Google Cloud
Run

– En el medical_prediction _local.htm modificar la url del servicio por la provista
por gcloud, este archivo lo pueden subir a un servidor web para darle acceso al
público, por ejemplo:

∗ https://diego-ramos.github.io/medical_api/medical_prediction.html
