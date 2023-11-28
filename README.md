# ProyectoArquitectura
Detector de latas usando YOLO V8


# Entrenamiento

Para entrenar el modelo debemos crear una carpeta en GoogleDrive, por ejemplo, "Colab Notebooks".
Luego, subimos los siguintes archivos:
- google_colab_config.yaml
- TrainYolov8CustomDataset.ipynb

Posteriormente subimos la carpeta "data" disponible en el siguiente link, la cual contiene nuestro dataset

https://drive.google.com/drive/folders/1hoRKcQNNuxM30iBF0TR2h6jpTavnMZQF?usp=sharing

Abrimos el segundo archivo con Google Colab, y ejecutamos cada linea para entrenar el modelo.

Finalmente descargamos el modelo ubicado en *runs/detect/train/weights/best.pt*
