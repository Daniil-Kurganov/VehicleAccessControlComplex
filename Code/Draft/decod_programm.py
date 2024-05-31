import cv2
import pytesseract
from imutils import contours
import time
import re
import pymysql

def Data_base_connection(inputValue: str) -> None:
    '''Функция подключения к БД и проверки наличия в ней государственного знака'''
    host, user, password, dbName = 'localhost', 'root', 'root', 'data_base_for_poeye'
    try:
        connection = pymysql.connect(host=host, port=3306, user=user, password=password, database=dbName, cursorclass=pymysql.cursors.DictCursor)
        print('Успешное подключение к базе данных.\n\n')
        try:
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM `car_plate_numbers`')
                table = cursor.fetchall()
                for row in table:
                    for element in re.findall(r'[A-Z][0-9]{3}[A-Z]{2}[0-9]{2,}', inputValue):
                        if element in row.values(): print('Считан номер ' + element + ', включённый в доверительный список. Доступ разрешён.\n')
        finally:
            connection.close()
    except Exception as ex:
        print('Связь с базой данный не установлена. Ошибка:', ex)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
cap = cv2.VideoCapture('pics/Test3.mp4')
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
finish = 0
while cap.isOpened():
    ret, frame = cap.read()
    start = time.time()
    if start - finish > 5:
        cv2.imwrite('pics/Current_frame.png', frame)
        image = cv2.imread('pics/Current_frame.png')
        height, width, _ = image.shape
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)[1]
        cntours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cntours, _ = contours.sort_contours(cntours[0])
        for element in cntours:
            area = cv2.contourArea(element)
            x, y, w, h = cv2.boundingRect(element)
            if area > 5000:
                img = image[y: y + h, x: x + w]
                result = pytesseract.image_to_string(img, lang = 'rus+eng', config = r"--oem 3 --psm 6 -c tessedit_char_whitelist=ABCEHKMOPTXY0123456789")
                if len(result) > 7: Data_base_connection(result)
        cv2.imshow('Окно вывода', thresh)
        finish = time.time()
    cv2.imshow('Test', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cap.release()
        break