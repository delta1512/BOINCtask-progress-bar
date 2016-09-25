# BOINCtask-progress-bar

Usage:

	1. Put server file on machine running BOINC
	
	2. Put the client file on the computer that drives the LEDs
	
	3. Change the required info on both scripts (Refer to comments, comments not labeled with "Optional:" must be changed)
	
	4. Run the server script and type the name of the slot folder number containing your desired task (In BOINCdata/slots/)
	
	5. Run the client script

I have tested the program with my ODroid C2 running wiringpi, controlling 10 LEDs.
The program works up until the task is completed. Then it requires the scripts to be run again.
Photo of my setup here: i.imgur.com/a2OGZwK.jpg
