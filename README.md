# ProyectoArquitectura
Detector de latas usando YOLO V8


# Entrenamiento

1) Para entrenar el modelo debemos importar nuestro dataset configurado en Roboflow en forma de directorio con nombre **"entrenamiento"**
a Google Drive, en la sección **"Mi unidad"**

2) A continuación, puede importar el archivo *Training.ipynb* al directorio **"entrenamiento"** y abrirlo en Google Colab o copiar el código
de dicho archivo, crear un notebook en el directorio **"entrenamiento"** y pegarlo ahí. 

3) Ejecutamos cada celda del notebook *Training.ipynb* y esperamos a que se entrene nuestro modelo con nuestro dataset.

4) Se creará un nuevo directorio "runs" y finalmente descargamos el modelo ubicado en *runs/detect/train/weights/best.pt*
