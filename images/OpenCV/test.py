import cv2 as cv
img = cv.imread("01.jpg", 0)
kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
dst = cv.dilate(img, kernel)
cv.imshow('src', img)
cv.imshow('dst', dst)
cv.waitKey(0)
