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