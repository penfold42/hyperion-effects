import hyperion, time, colorsys, random

# Get the parameters
sleepTime = float(hyperion.args.get('AsleepTime', 0.01))
color = hyperion.args.get('color', (255,0,0))
text = hyperion.args.get('text', "Hello World")

# Check parameters

# Initialize the led data
width = 150
height = 5
imageData = bytearray(height * width * (0,0,0))


def ascii_to_offset(char):
	chr = ord(char)
# symbnols, numbers, capital letters
	if (chr>=0x20) and (chr<0x5b):
		return chr-0x20;
# lower case letters
	elif (chr>=0x61) and (chr<=0x7a):
		return chr-0x40;
	else:
		return 0xff;

def setPixel(x,y,rgb):
        global imageData, width
        offset = y*width*3 + x*3
        if offset+2 < len(imageData):
                imageData[offset]   = rgb[0]
                imageData[offset+1] = rgb[1]
                imageData[offset+2] = rgb[2]

def randomColor():
#	color = colorsys.hsv_to_rgb(random.random() ,1, 1)

	hue = sat = val = 1.0
	hue = random.uniform(0, 0.999999)
#	sat = random.random()
	val = random.uniform(0.5, 0.9999)
	color = colorsys.hsv_to_rgb(hue, sat, val)
	color = ( int(color[0]*255), int(color[1]*255), int(color[2]*255) )
	return color;

def stripe_lr(y):
	global height, width, imageData
	color = randomColor()
	for x in range(0,width):
		setPixel(x,y,color)
		hyperion.setImage(width, height, imageData)
		time.sleep(sleepTime)

def stripe_rl(y):
	global height, width, imageData
	color = randomColor()
	for x in range(width-1, -1, -1):
		setPixel(x,y,color)
		hyperion.setImage(width, height, imageData)
		time.sleep(sleepTime)


while not hyperion.abort():
#	for y in range(0,height):
	y = random.randrange(0,height)
	if random.random() > 0.5:
		stripe_lr(y)
	else:
		stripe_rl(y)


