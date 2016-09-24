import sys
import socket
import time

print('Slot number: ')
num = sys.stdin.readline(1)
#Put the directory to the BOINC data folder in '[rest of directory]'
location = '[rest of directory]/slots/' + num + '/boinc_task_state.xml'
input = open(location, 'r')

#Optional:
#Change socket info and port number here
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
host = socket.gethostname()
port = 12345                
s.bind((host, port))

s.listen(5)   
c, addr = s.accept()              
while True:
	input = open(location, 'r')
	lines = input.readlines()
	completion = lines[5]
	val = str(completion[19:23])
	input.close()
	c.sendall(val.encode())
	#Optional:
	#Change update frequency (seconds)
	#Note: keep frequency values the same in the server script and the client script
	time.sleep(10)              