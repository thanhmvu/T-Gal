import os
import numpy as np
import cv2

SRC = "./images/fulls/"
DST = "./images/thumbs/"
start = 1
end = 22
W = 360
HoW = 0.625

def createThumbs():
	# read file in this dir
	for i in range (start, end + 1):
		img = cv2.imread(SRC + `i`.zfill(2) + '.jpg')
		h,w = img.shape[:2]

		if w*HoW < h:
			img = img[int((h-w*HoW)/2) : int((h+w*HoW)/2) , :]
		else:
			img = img[: , int((w-h/HoW)/2) : int((w+h/HoW)/2)]

		img = cv2.resize(img,(W,int(W*HoW)))

		cv2.imwrite(DST+ `i`.zfill(2) + '.jpg', img)
		print (i)

createThumbs()