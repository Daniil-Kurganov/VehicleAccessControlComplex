import cv2
from imageai.Detection import ObjectDetection
import time

cap = cv2.VideoCapture("pics/test.mp4")
detector = ObjectDetection()
detector.setModelTypeAsTinyYOLOv3()
detector.setModelPath('yolo-tiny.h5')
detector.loadModel()
finish = 0
while cap.isOpened():
    ret, image = cap.read()
    start = time.time()
    if start - finish > 10:
        _, array_detection = detector.detectObjectsFromImage(input_image = image, input_type = "array",output_type = 'array')
        finish = time.time()
        print(array_detection)
    cv2.imshow("Window", image)
    if cv2.waitKey(30) == 27:
        break
cap.release()
cv2.destroyAllWindows()