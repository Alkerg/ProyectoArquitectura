# ProyectoArquitectura
Detector de latas usando YOLO V8


# Entrenamiento

Para entrenar el modelo debemos importar nuestro dataset en forma de directorio con nombre "entrenamiento",
a continuación, creamos un notebook con Google Colaboratory y lo guardamos en el directorio "entrenamiento".

Posteriormente subimos la carpeta "data" disponible en el siguiente link, la cual contiene nuestro dataset

https://drive.google.com/drive/folders/1hoRKcQNNuxM30iBF0TR2h6jpTavnMZQF?usp=sharing

Abrimos el archivo *TrainYolov8CustomDataset.ipynb* con Google Colab, y ejecutamos cada linea para entrenar el modelo.

Finalmente descargamos el modelo ubicado en *runs/detect/train/weights/best.pt*
