import wiringpi2 as wpi
import socket
import time

#Change GPIO address values for your board here
leds = [7, 0, 1, 4, 5, 6, 10, 11, 26, 27]

wpi.wiringPiSetup()

for x in leds:
	wpi.pinMode(x, 1)
	wpi.digitalWrite(x, 0)
#Optional:
#Change socket info and port number here
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345

#Put the name of the computer running the server under 'localhost'
s.connect(('localhost', 12345))
while True:
    for x in leds:
        wpi.digitalWrite(x, 0)
    val = float(s.recv(1024).decode())
    final = round(val * 10)

    ledcount = int(final)
    i = 0
    while ledcount >= 1:
	    led = leds[i]
	    wpi.digitalWrite(led, 1)
	    i = i + 1
	    ledcount = ledcount - 1
	#Optional:
	#Change update frequency (seconds)
	#Note: keep frequency values the same in the server script and the client script
    time.sleep(10)
