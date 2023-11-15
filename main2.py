from ultralytics import YOLO
import cv2

model = YOLO("runs/detect/train/weights/bestCanBottle.pt")

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    ret,frame = cap.read()
    model.predict(frame, show=True, conf=0.9)

    exitKey = cv2.waitKey(5)

    if(exitKey == 27):
        break


cap.release()
cv2.destroyAllWindows()