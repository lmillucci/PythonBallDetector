#!/usr/bin/env python

import cv

mainGui="Immagine acquisita"
hsvWindow="Immagine HSV"
thresholdWindow="Immagine rilevata"
settingWindow="Imposta soglia"
blurWindow="Immagine con filtro Blur"

cv.NamedWindow("Immagine acquisita",1)
#imposto la sorgente per l'acquisizione
# 0 -> cam predefinita
# 1 -> cam esterna
capture = cv.CaptureFromCAM(0);


#loop principale del programma
while True:
	#definisco la variabile per i frame catturati
	cameraFeed = cv.QueryFrame(capture)
	#definisco la variabile che contiene i frame HSV
	hsvFrame = cv.CreateImage(cv.GetSize(cameraFeed),8,3)
	
	#conversione del colore in HSV
	cv.CvtColor(cameraFeed, hsvFrame, cv.CV_BGR2HSV)
	
	
	#visualizzo le immagini 
	cv.ShowImage(mainGui,cameraFeed)
	cv.ShowImage(hsvWindow, hsvFrame)
	
	if cv.WaitKey(33)==27:
		break
	
