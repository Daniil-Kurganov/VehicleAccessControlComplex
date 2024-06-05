import multiprocessing
import time
import math
from tkinter import Tk
import cv2
import multiprocessing as mp

import numpy as np

from GUI import *

def current_camera_video_show() -> None:
    '''Иммитация вывода видео с соответствующей камеры'''
    ret, frame = video_capture.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (431, 261), interpolation = cv2.INTER_AREA)
        qimage = qimage2ndarray.array2qimage(frame)
        ui.LabelCameraVideo.clear()
        ui.LabelCameraVideo.setPixmap(QtGui.QPixmap.fromImage(qimage))
    return None
def start_show_camera_video() -> None:
    '''Запуск таймера и показ таймера'''
    global video_capture, count_of_frame_show
    camera_index = ui.ComboBox.currentIndex()
    video_capture = cv2.VideoCapture()
    video_capture.open('C:/Users/User/PythonProjects/VehicleAccessControlComplex/Sources/Media/ResultVideos/{}.mp4'.format(camera_index))
    ui.timer = QtCore.QTimer()
    ui.timer.setInterval(33)
    ui.timer.timeout.connect(current_camera_video_show)
    ui.timer.start()
    if camera_index == 2:
        count_of_frame_show = 0
        ui.timer0 = QtCore.QTimer()
        ui.timer0.setInterval(7000)
        ui.timer0.timeout.connect(show_car_plate_number)
        ui.timer0.start()
        # ui.timer1 = QtCore.QTimer()
        # ui.timer1.setInterval(48000)
        # ui.timer1.timeout.connect(current_camera_video_show)
        # ui.timer1.start()
        # ui.timer2 = QtCore.QTimer()
        # ui.timer2.setInterval(109000)
        # ui.timer2.timeout.connect(current_camera_video_show)
        # ui.timer2.start()
    return None
def show_car_plate_number() -> None:
    '''Демонстрация распознанного знака'''
    global count_of_frame_show
    if count_of_frame_show == 0:
        ui.LabelTraficLights.setPixmap(QtGui.QPixmap.fromImage(qimages_TF[1]))
        ui.LabelPlateNumberFrame.setPixmap(QtGui.QPixmap.fromImage(preparing_car_plate_frame(0)))
        ui.LabelTraficLights.setPixmap(QtGui.QPixmap.fromImage(qimages_TF[2]))
        ui.timer0.setInterval(38000)
    elif count_of_frame_show == 1:
        ui.LabelTraficLights.setPixmap(QtGui.QPixmap.fromImage(qimages_TF[1]))
        ui.LabelPlateNumberFrame.setPixmap(QtGui.QPixmap.fromImage(preparing_car_plate_frame(1)))
        ui.LabelTraficLights.setPixmap(QtGui.QPixmap.fromImage(qimages_TF[0]))
        ui.timer0.setInterval(68000)
    else:
        ui.LabelTraficLights.setPixmap(QtGui.QPixmap.fromImage(qimages_TF[1]))
        ui.LabelPlateNumberFrame.setPixmap(QtGui.QPixmap.fromImage(preparing_car_plate_frame(2)))
        ui.LabelTraficLights.setPixmap(QtGui.QPixmap.fromImage(qimages_TF[2]))
    count_of_frame_show += 1
    return None
def preparing_car_plate_frame(frame_index: int) -> qimage2ndarray.array2qimage:
    '''Преобразования текущего кадра знака'''
    image = cv2.imread('C:/Users/User/PythonProjects/VehicleAccessControlComplex/Sources/Media/DetectedCarPlateFrames/{}.png'.format(frame_index))
    turn_angle = int(math.degrees(math.atan((image.shape[0] - 30) / image.shape[1])))
    (h, w) = image.shape[:2]
    center = (int(w / 2), int(h / 2))
    rotation_matrix = cv2.getRotationMatrix2D(center, turn_angle, scale=1)
    image = cv2.warpAffine(image, rotation_matrix, (w, h))[image.shape[0] // 2 - 20: image.shape[0] // 2 + 20, :]
    cv2.imwrite('C:/Users/User/PythonProjects/VehicleAccessControlComplex/Sources/Media/Heap/res.png', image)
    image = np.asarray(Image.open('C:/Users/User/PythonProjects/VehicleAccessControlComplex/Sources/Media/Heap/res.png').convert('RGB'))
    image = np.asarray(Image.fromarray(image.astype('uint8'), 'RGB').resize((231, 61)))
    return qimage2ndarray.array2qimage(image)

if __name__ == "__main__":
    qimages_TF = []
    for current_image_name in ['Red', 'Yellow', 'Green']:
        current_image = np.asarray(Image.open('C:/Users/User/PythonProjects/VehicleAccessControlComplex/Sources/Media/'
                                              'TraficLights/{}.jpg'.format(current_image_name)).convert('RGB'))
        current_image = np.asarray(Image.fromarray(current_image.astype('uint8'), 'RGB').resize((189, 61)))
        qimage_current = qimage2ndarray.array2qimage(current_image)
        qimages_TF.append(qimage_current)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.LabelTraficLights.setPixmap(QtGui.QPixmap.fromImage(qimages_TF[0]))
    ui.ComboBox.currentIndexChanged.connect(start_show_camera_video)
    sys.exit(app.exec_())