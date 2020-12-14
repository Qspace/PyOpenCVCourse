"""
Chuong trinh nhan 2 tham so truyen vao la duong dan toi bg va fg img,
Xac dinh va ve hinh chu nhat bao quanh khu vuc khac biet
"""

import argparse
import cv2
import numpy as np


# Xay dung list argument
argP = argparse.ArgumentParser()
argP.add_argument("-b", "--bgImg", required=True,
    help="path to back ground image")
argP.add_argument("-f", "--fgImg", required=True,
    help="path to fore ground image")

args = vars(argP.parse_args())

# Tai anh len
bgImg = cv2.imread(args["bgImg"])
fgImg = cv2.imread(args["fgImg"])


# chuyen sang gray scale 0-255
bgGrayImg = cv2.cvtColor(bgImg, cv2.COLOR_BGR2GRAY)
fgGrayImg = cv2.cvtColor(fgImg, cv2.COLOR_BGR2GRAY)

# cv2.imshow("bg", bgGrayImg)
# cv2.imshow("fg", fgGrayImg)
# cv2.waitKey(0)


# Tru 2 anh
# (0,255) - (0,255) ===>(-255,255)==> chuyen ve gia tri duong (0,255)
# bang cach lay tri tuyet doi
subImg = bgGrayImg.astype("int32") - fgGrayImg.astype("int32")
subImg = np.absolute(subImg).astype("uint8")
cv2.imshow("fg", subImg)
cv2.waitKey(0)

# # Tao binary image
threSholdImg = cv2.threshold(subImg, 0 , 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
cv2.imshow("fg", threSholdImg)
cv2.waitKey(0)


# #Loai bo nhieu
# threSholdImg = cv2.erode(threSholdImg, None, iterations=1)
# threSholdImg = cv2.dilate(threSholdImg, None, iterations=1)
# # cv2.imshow("fg", threSholdImg)
# # cv2.waitKey(0)

# #Thuc hien giai thuat contours de noi cac diem anh danh dau tren binary image de tao
# #duong bao 
# # Contours no se tra ve list cac diem (x,y) tren duong bao
# cntrsPoint =cv2.findContours(threSholdImg.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# cntrsPoint = cntrsPoint[0]
# # cv2.drawContours(threSholdImg, cntrsPoint, -1, (0,255,0), 3

# cv2.imshow("ct", threSholdImg)
# cv2.waitKey(0)

# (minX, minY) = (np.inf, np.inf)
# (maxX, maxY) = (-np.inf, -np.inf)

# #Loop tat cac item trong countours de xac dinh duoc vi tri bat dau v ket thuc cua hcn bao
# for c in cntrsPoint:
#     # xac dinh hcn bao quanh moi item
#     (x,y,w,h) = cv2.boundingRect(c)

#     minX = min(minX,x)
#     minY = min(minY,y)
#     maxX = max(maxX, x+w-1)
#     maxY = max(maxY, y+h-1)


# # Ve hcn bao quanh khu vuc khac biet giua 2 anh
# cv2.rectangle(fgImg, (minX, minY), (maxX,maxY), (255,0,0), 5)

# #show img
# cv2.imshow("Output Img", fgImg)
# cv2.waitKey(0)