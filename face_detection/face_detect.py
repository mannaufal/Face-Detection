#Import Library OpenCV
import cv2

#Membuka file cascade.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Membaca input foto
img = cv2.imread('IMG4.jpg')

#Konversi kedalam greyscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Deteksi wajah
faces = face_cascade.detectMultiScale(gray, 1.25, 4)

#Kotak Persegi
for (x, y, w, h) in faces:
	cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)

#Output
cv2.imshow('img', img)
cv2.waitKey()