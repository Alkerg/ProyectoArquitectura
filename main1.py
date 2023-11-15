from ultralytics import YOLO
import cv2

model = YOLO("runs/detect/train/weights/bestCanBottle.pt")

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:

    ret,frame = cap.read()

    results = model.predict(frame, imgsz=640, conf=0.9)

    annotations = results[0].plot()

    cv2.imshow("Deteccion y segmentacion", annotations)

    exitKey = cv2.waitKey(5)

    if exitKey == 27:
        break

cap.release()
cv2.destroyAllWindows()

