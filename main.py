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


#loop principale del programma
while True:
	#definisco la variabile per i frame catturati
	_,cameraFeed = capture.read()
	cameraFeed = cv2.flip(cameraFeed,1)


	createSlider()

	colorMin=np.array([H_MIN,S_MIN,V_MIN],np.uint8)
	#filtro hsvFrame cercando solo un determinato range di colori
	#cv2.InRange(hsvFrame, colorMin, colorMin,thresholded);
	
	
	#visualizzo le immagini 
	cv2.imshow(mainGui,cameraFeed)
	#cv2.ShowImage(hsvWindow, hsvFrame)
	
	if cv2.waitKey(33)==27:
		break
	
