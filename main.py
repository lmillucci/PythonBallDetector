#!/usr/bin/env python
import numpy as np
import cv2

#------ VALORI PREDEFINITI --------
H_MIN = 26
S_MIN = 75
V_MIN = 67
H_MAX = 256
S_MAX = 256
V_MAX = 256

#------ FINESTRE -----------
mainGui="Immagine acquisita"
hsvWindow="Immagine HSV"
thresholdWindow="Immagine rilevata"
settingWindow="Imposta soglia"
blurWindow="Immagine con filtro Blur"

def onTrackbarSlide(*args):
    pass




def createSlider():
	
	cv2.namedWindow(settingWindow,1);
	
	#metodo che crea le trackbar(label, finestra, valore da cambiare, valore massimo,action listener)
	cv2.createTrackbar("H-min",settingWindow, H_MIN, 256, onTrackbarSlide)
	cv2.createTrackbar("S-min",settingWindow, S_MIN, 256,onTrackbarSlide)
	cv2.createTrackbar("V-min",settingWindow, V_MIN, 256,onTrackbarSlide)
	cv2.createTrackbar("H-max",settingWindow, H_MAX, 256, onTrackbarSlide)
	cv2.createTrackbar("S-max",settingWindow, S_MAX, 256,onTrackbarSlide)
	cv2.createTrackbar("V-max",settingWindow, V_MAX, 256,onTrackbarSlide)
	


# ------- MAIN -------------


cv2.namedWindow(mainGui,1)
#imposto la sorgente per l'acquisizione
# 0 -> cam predefinita
# 1 -> cam esterna
capture = cv2.VideoCapture(0);
width,height = capture.get(3),capture.get(4)

createSlider()
#loop principale del programma
while True:
	#definisco la variabile per i frame catturati
	_,cameraFeed = capture.read()
	cameraFeed = cv2.flip(cameraFeed,1)
	
	#variabile su cui salvo l'immagine HSV
	hsvFrame = cv2.cvtColor(cameraFeed,cv2.COLOR_BGR2HSV)


	

	#filtro hsvFrame cercando solo un determinato range di colori
	minColor=np.array((cv2.getTrackbarPos("H-min",settingWindow),cv2.getTrackbarPos("S-min",settingWindow),cv2.getTrackbarPos("V-min",settingWindow)))
	maxColor=np.array((cv2.getTrackbarPos("H-max",settingWindow),cv2.getTrackbarPos("S-max",settingWindow),cv2.getTrackbarPos("V-max",settingWindow)))
	thresholded=cv2.inRange(hsvFrame,minColor, maxColor);
	
	
	#visualizzo le immagini 
	cv2.imshow(mainGui,cameraFeed)
	#cv2.imshow(hsvWindow, hsvFrame)
	cv2.imshow(thresholdWindow,thresholded)
	
	if cv2.waitKey(33)==27:
		break
	
