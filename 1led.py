import hyperion
import time
import colorsys

# Get the parameters
whichLed = int(hyperion.args.get('whichLed', 1))
whichColour = hyperion.args.get('whichColour', "ff00ff")
sleepTime = float(hyperion.args.get('sleepTime', 1.0))

if (len(whichColour) == 6):
	red = int(whichColour[0:2],16)
	green = int(whichColour[2:4],16)
	blue = int(whichColour[4:6],16)
	# Start the write data loop
	while not hyperion.abort():
		ledData = bytearray()
		for i in range(hyperion.ledCount):
			if (i==whichLed):
				ledData += bytearray((int(red), int(green), int(blue))) 
			else:
				ledData += bytearray((int(0), int(0), int(0))) 
		hyperion.setColor(ledData)
		time.sleep(sleepTime)


