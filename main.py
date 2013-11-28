#!/usr/bin/env python

import cv


cv.NamedWindow("Immagine acquisita",1)
#imposto la sorgente per l'acquisizione
# 0 -> cam predefinita
# 1 -> cam esterna
capture = cv.CaptureFromCAM(0);


#loop principale del programma
while True:
	cameraFeed = cv.QueryFrame(capture)
	
	
	#visualizzo le immagini 
	cv.ShowImage("Immagine acquisita",cameraFeed)
	
	if cv.WaitKey(33)==27:
		break
	
