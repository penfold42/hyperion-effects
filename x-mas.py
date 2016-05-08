import hyperion
import time
import colorsys

# Get the parameters
sleepTime = float(hyperion.args.get('sleepTime', 1.0))

# Initialize the led data
ledData0 = bytearray()
for i in range(hyperion.ledCount):
	if i%3 == 0:
		ledData0 += bytearray((int(255), int(0), int(0)))
	if i%3 == 1:
		ledData0 += bytearray((int(255), int(255), int(255)))
	if i%3 == 2:
		ledData0 += bytearray((int(0), int(255), int(0)))
		
ledData1 = bytearray()
for i in range(hyperion.ledCount):
	if i%3 == 0:
		ledData1 += bytearray((int(255), int(255), int(255)))
	if i%3 == 1:
		ledData1 += bytearray((int(0), int(255), int(0)))
	if i%3 == 2:
		ledData1 += bytearray((int(255), int(0), int(0)))

ledData2 = bytearray()
for i in range(hyperion.ledCount):
	if i%3 == 0:
		ledData2 += bytearray((int(0), int(255), int(0)))
	if i%3 == 1:
		ledData2 += bytearray((int(255), int(0), int(0)))
	if i%3 == 2:
		ledData2 += bytearray((int(255), int(255), int(255)))

# Start the write data loop
while not hyperion.abort():
	hyperion.setColor(ledData0)
	time.sleep(sleepTime)
	hyperion.setColor(ledData1)
	time.sleep(sleepTime)
	hyperion.setColor(ledData2)
	time.sleep(sleepTime)
