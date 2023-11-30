from ultralytics import YOLO
import cv2

model = YOLO("modelos/modelo.pt")

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:

    ret,frame = cap.read()

    results = model.predict(frame, imgsz=640, conf=0.9)

    annotations = results[0].plot()

    cv2.imshow("Detector de latas", annotations)

    exitKey = cv2.waitKey(1)

    if exitKey == 27:
        break

cap.release()
cv2.destroyAllWindows()

