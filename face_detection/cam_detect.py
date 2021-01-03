#import library
import cv2

#Membuka file cascade.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Membuka web cam
cap = cv2.VideoCapture(0)

while True:
	_, img = cap.read()
	#konversi ke graysclae
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	#Mendeteksi wajah
	faces = face_cascade.detectMultiScale(gray, 1.09, 4)
	#membuat kotak
	for (x, y, w, h) in faces:
		cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
		#Display
		cv2.imshow('img',img)
		#stop if escape button is pressed
		k = cv2.waitKey(360) & 0xff
		if k == 357:
			break
#Release
cap.release()