import cv2
import pytesseract
import math
import numpy as np

array_image = cv2.imread('C:/Users/User/PythonProjects/VehicleAccessControlComplex/Sources/Media/DetectedCarPlateFrames/PlateFrame1029.png')
turn_angle = int(math.degrees(math.atan((array_image.shape[0] - 30) / array_image.shape[1])))
print(turn_angle)
(h, w) = array_image.shape[:2]
center = (int(w / 2), int(h / 2))
rotation_matrix = cv2.getRotationMatrix2D(center, turn_angle, scale = 1)
rotated = cv2.warpAffine(array_image, rotation_matrix, (w, h))[array_image.shape[0] // 2 - 15 : array_image.shape[0] // 2 + 15, :]
# rotated = rotated[:, -40:]
cv2.imwrite('C:/Users/User/PythonProjects/VehicleAccessControlComplex/Sources/Media/res.png', rotated)
result = pytesseract.image_to_string(rotated, lang = 'eng', config = r"--oem 3 --psm 11 -c tessedit_char_whitelist=ABCEHKMOPTXY0123456789")
print(result)
result = pytesseract.image_to_string(rotated, lang = 'eng', config = r"--oem 3 --psm 7 -c tessedit_char_whitelist=ABCEHKMOPTXY0123456789")
print(result)
result = pytesseract.image_to_string(rotated, lang = 'eng', config = r"--oem 3 --psm 13 -c tessedit_char_whitelist=ABCEHKMOPTXY0123456789")
print(result)
result = pytesseract.image_to_string(rotated, lang = 'eng', config = r"--oem 3 --psm 12 -c tessedit_char_whitelist=ABCEHKMOPTXY0123456789")
print(result)



# Побуквенное выделение
# ar_trim = np.linspace(0, fpart.shape[1], 7, dtype = int)
# for ind in range(len(ar_trim) - 1):
#     # if ar_trim[ind] != 0: fp = ar_trim[ind] - 5
#     # else: fp = 0
#     fpart1 = fpart.copy()
#     fpart1[:, ar_trim[ind + 1]:] = 0
#     fpart1[:, :ar_trim[ind]] = 0
#     cv2.imwrite('C:/Users/User/PythonProjects/VehicleAccessControlComplex/sources/{}.png'.format(ind), fpart1)
#     result = pytesseract.image_to_string(fpart1, config = r"--oem 3 --psm 11 -c tessedit_char_whitelist=ABCEHKMOPTXY0123456789")
#     print(result)
#     result = pytesseract.image_to_string(fpart1, config = r"--oem 3 --psm 7 -c tessedit_char_whitelist=ABCEHKMOPTXY0123456789")
#     print(result)
#     result = pytesseract.image_to_string(fpart1, config = r"--oem 3 --psm 13 -c tessedit_char_whitelist=ABCEHKMOPTXY0123456789")
#     print(result)
#     result = pytesseract.image_to_string(fpart1, config = r"--oem 3 --psm 12 -c tessedit_char_whitelist=ABCEHKMOPTXY0123456789")
#     print(result)
#     print(ind)
#     print('-----------------------------')



# Поворот изображения
# array_image = cv2.imread('C:/Users/User/PythonProjects/VehicleAccessControlComplex/sources/frame0911.png')
# turn_angle = int(math.degrees(math.atan((array_image.shape[0] - 30) / array_image.shape[1])))
# print(turn_angle)
# (h, w) = array_image.shape[:2]
# center = (int(w / 2), int(h / 2))
# rotation_matrix = cv2.getRotationMatrix2D(center, turn_angle, scale = 1)
# rotated = cv2.warpAffine(array_image, rotation_matrix, (w, h))



# Решительный вариант детекции
# image = cv2.imread('C:/Users/User/PythonProjects/VehicleAccessControlComplex/Sources/Media/DetectedCarPlateFrames/PlateFrame361.png')
# result = pytesseract.image_to_string(image, lang = 'eng', config = r"--oem 3 --psm 11 -c tessedit_char_whitelist=ABCEHKMOPTXY0123456789")
# print(result)
# result = pytesseract.image_to_string(image, lang = 'eng', config = r"--oem 3 --psm 7 -c tessedit_char_whitelist=ABCEHKMOPTXY0123456789")
# print(result)
# result = pytesseract.image_to_string(image, lang = 'eng', config = r"--oem 3 --psm 13 -c tessedit_char_whitelist=ABCEHKMOPTXY0123456789")
# print(result)
# result = pytesseract.image_to_string(image, lang = 'eng', config = r"--oem 3 --psm 12 -c tessedit_char_whitelist=ABCEHKMOPTXY0123456789")
# print(result)



# Устаревшая детекция
# height, width, _ = image.shape
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)[1]
# cntours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cntours, _ = contours.sort_contours(cntours[0])
# for element in cntours:
#     area = cv2.contourArea(element)
#     x, y, w, h = cv2.boundingRect(element)
#     img = image[y: y + h, x: x + w]
#     result = pytesseract.image_to_string(img, lang = 'rus+eng', config = r"--oem 3 --psm 6 -c tessedit_char_whitelist=ABCEHKMOPTXY0123456789")
#     print(result)