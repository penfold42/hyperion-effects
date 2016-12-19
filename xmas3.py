import hyperion
import time
import colorsys

# Get the parameters
sleepTime = float(hyperion.args.get('sleepTime', 1.0))
colorOne = hyperion.args.get('color_one', (255,0,0))
colorTwo = hyperion.args.get('color_two', (0,255,0))
colorThree = hyperion.args.get('color_three', (255,255,255))
# Initialize the led data
ledDataOdd = bytearray()
for i in range(hyperion.ledCount):
	if i%3 == 0:
		ledDataOdd += bytearray(colorOne)
	if i%3 == 1:
                ledDataOdd += bytearray(colorTwo)
        if i%3 == 2:
                ledDataOdd += bytearray(colorThree)
		
ledDataEven = bytearray()
for i in range(hyperion.ledCount):
        if i%3 == 0:
                ledDataEven += bytearray(colorThree)
	if i%3 == 1:
		ledDataEven += bytearray(colorOne)
	if i%3 == 2:
		ledDataEven += bytearray(colorTwo)
ledDataThirdWheel = bytearray()
for i in range(hyperion.ledCount):
        if i%3 == 0:
                ledDataThirdWheel += bytearray(colorTwo)
	if i%3 == 1:
		ledDataThirdWheel += bytearray(colorThree)
	if i%3 == 2:
		ledDataThirdWheel += bytearray(colorOne)

# Start the write data loop
while not hyperion.abort():
	hyperion.setColor(ledDataOdd)
	time.sleep(sleepTime)
	hyperion.setColor(ledDataEven)
	time.sleep(sleepTime)
	hyperion.setColor(ledDataThirdWheel)
	time.sleep(sleepTime)
