import cv2 as cv

img = cv.imread('sixpeople.jfif')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.05, minNeighbors = 3)

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (255,0,0), thickness = 2)

cv.imshow('Faces Detected',img) 

cv.waitKey(0)