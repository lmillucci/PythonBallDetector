import bluetooth
import RPi.GPIO as io

target=320

io.setmode(io.BCM)

io.cleanup() 

in1_pin = 4
in2_pin = 17
pwm_pin= 23
in3_pin = 24
in4_pin = 25
pwm2_pin = 22
 
io.setup(in1_pin, io.OUT)
io.setup(in2_pin, io.OUT)
io.setup(pwm_pin, io.OUT)
io.setup(in3_pin, io.OUT)
io.setup(in4_pin, io.OUT)
io.setup(pwm2_pin, io.OUT)
p=io.PWM(pwm_pin, 500)
q=io.PWM(pwm2_pin, 500)

p.start(0)
p.ChangeDutyCycle(0)
q.start(0)
q.ChangeDutyCycle(0)




def changeSpeed(value1, value2 ):
	p.ChangeDutyCycle(value1)
	q.ChangeDutyCycle(value2)

 #motore 1
def motor1Orario():
    io.output(in1_pin, True)    
    io.output(in2_pin, False)
 
def motor1AntiOrario():
    io.output(in1_pin, False)
    io.output(in2_pin, True)
#motore 2
def motor2Orario():
	io.output(in3_pin,True)
	io.output(in4_pin,False)
	
def motor2AntiOrario():
	io.output(in3_pin,False)
	io.output(in4_pin,True)



def passaggioDati(data):
	line=data.split(";")
	x_tmp=line[0]
	y_tmp=line[1]
	x=(int)(x_tmp)
	y=(int)(y_tmp)
	print "Messaggio ricevuto="+str(x)+";"+str(y)
	if x>0 and y>0:
		controllerMotori(x,y)
	else:
		changeSpeed(0,0)
		
def controllerMotori(x,y):
			
		e = (int)(x)-target #variabile errore >0 oggetto a dx
									#<0 oggetto a sx
		Kp=100
		u = int(Kp * (abs(e)/(target *1.0)))

		changeSpeed(u,u)
		print "Valocita = "+str(u)+ " errore = "+str(e)+ " abs = "+str(abs(e)/(target*1.0))
		
		#decido la direzione da prendere. Uso +-10 e non 0 per avere un minimo di tolleranza
		if e < -40:
			#giro a dx
			print "giro sx"
			motor1AntiOrario()
			motor2AntiOrario()

		elif e > 40:
			#giro a dx
			print "giro dx"
			motor1Orario()
			motor2Orario()


		else:
			#vado avanti
			print "vado avanti"
			changeSpeed(80,80)
			motor2Orario()
			motor1AntiOrario()
			#motor1AntiOrario()
			#motor2AntiOrario()


server_sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)

port = 5
server_sock.bind(("",port))
server_sock.listen(1)

try:
	client_sock,address = server_sock.accept()
	print "Accepted connection from ",address
	while True:
		data=client_sock.recv(1024)
		if data:		
			#print "Received [%s]" % data
			passaggioDati(data)
			
except Exception as e:	
	print "EXCEPTION: closing connection"	
	client_sock.close()
	server_sock.close()
	io.cleanup() 
	print e


