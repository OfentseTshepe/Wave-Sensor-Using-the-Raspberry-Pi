from datetime import datetime
import spidev
import time
import threading
import RPi.GPIO as GPIO
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000


GPIO.setmode(GPIO.BCM)

import socket

port= 1666
server='197.239.163.40'
wave_sensor= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
wave_sensor.connect((server,port))

def ADC(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  adc_val = ((adc[1]&3) << 8) + adc[2]
  return adc_val




def LightReadding(adc_val):
  volts = (adc_val * 3.3) / float(1023)
  volts = round(volts,1)
  return  volts





light=6

Light_value =0
Lightwave =0
Period="0"
total=0
def Count():
	global Lightwave
	global Period
	global total
	time.sleep(0.05)
	now= Lightwave
	Period=""
	duration=datetime.now()
	while True:
		time.sleep(0.2)
		value=Lightwave
		if(value>1):
			total+=1
			Period=str(datetime.now()-duration)[3:-4]
			duration=datetime.now()
			time.sleep(0.2)


Thread2=threading.Thread(target=Count)

def Sample():
	global Lightwave
	global total
	global wave_sensor
	global Period
	while True:

		Light_value = ADC(light)
		Lightwave = LightReadding(Light_value)
		time.sleep(0.3)
		print(Lightwave," ",Period)
		wave_sensor.send(str.encode("number of waves: "+str(total)+" light percentage: "+str(round(Lightwave/3.3*100,2))+" wave speed"+str(Period)))
		
Thread1=threading.Thread(target=Sample)

Thread1.start()
Thread2.start()