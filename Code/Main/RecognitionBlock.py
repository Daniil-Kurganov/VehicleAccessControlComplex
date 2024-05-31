import cv2
import numpy as np
import pytesseract
import math

def plate_frame_recognition(array_frame: np.array) -> list:
    '''Функция препроцессинга и распознования автомобильного номера'''
    turn_angle = int(math.degrees(math.atan((array_frame.shape[0] - 30) / array_frame.shape[1])))
    (h, w) = array_frame.shape[:2]
    center = (int(w / 2), int(h / 2))
    rotation_matrix = cv2.getRotationMatrix2D(center, turn_angle, scale = 1)
    rotated = cv2.warpAffine(array_frame, rotation_matrix, (w, h))[array_frame.shape[0] // 2 - 20 : array_frame.shape[0] // 2 + 20, :]
    cv2.imwrite('C:/Users/User/PythonProjects/VehicleAccessControlComplex/Sources/Media/res.png', rotated)
    list_recognition_results = []
    list_recognition_results.append(pytesseract.image_to_string(rotated, lang = 'eng',
                                                                config = r"--oem 3 --psm 11 -c tessedit_char_whitelist=ABCEHKMOPTXY0123456789")[:-1])
    list_recognition_results.append(pytesseract.image_to_string(rotated, lang = 'eng',
                                                                config = r"--oem 3 --psm 7 -c tessedit_char_whitelist=ABCEHKMOPTXY0123456789")[:-1])
    list_recognition_results.append(pytesseract.image_to_string(rotated, lang = 'eng',
                                                                config = r"--oem 3 --psm 13 -c tessedit_char_whitelist=ABCEHKMOPTXY0123456789")[:-1])
    list_recognition_results.append(pytesseract.image_to_string(rotated, lang = 'eng',
                                                                config = r"--oem 3 --psm 12 -c tessedit_char_whitelist=ABCEHKMOPTXY0123456789")[:-1])
    return list_recognition_results

if __name__ == '__main__':
    array_frame = cv2.imread('C:/Users/User/PythonProjects/VehicleAccessControlComplex/Sources/Media/DetectedCarPlateFrames/PlateFrame1029.png')
    print(plate_frame_recognition(array_frame))