import time
import bluetooth

btAddress="00:18:E4:09:02:45"
#btAddress="00:22:43:F2:4A:9F"

port = 5

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((btAddress, port))

print "Invio"

i=0
while True:
	inFile=open("coordinate.txt","r")
	line=inFile.read().split(';')
	x=line[0]
	y=line[1]
	message = str(x)+";"+str(y)
	sock.send(message)
	time.sleep(0.5)
	i+=1
	inFile.close()
	
	print message
	
sock.close()






