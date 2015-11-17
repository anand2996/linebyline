add_library('serial')
add_library('arduino')

ard = Arduino(this,"COM4",57600)
 
def setup():
    global ard
    size(480,640)
    img = loadImage("bg1.jpg")
    background(img)
    frameRate(30)
    #Serial.begin(9600)
    #ard.pinMode(0,ard.INPUT)
    #ard.pinMode(13, ard.OUTPUT)
 
def draw():
    global ard
    sensor = ard.analogRead(0)
    if (sensor > 99):
        background(123)
        rect(50, 50, 100, 100)
        fill(154)
    if (sensor > 129):
        background(143)
        rect(60, 60, 110, 110)
        fill(134)
    if (sensor > 159):
        background(163)
        rect(70, 70, 120, 120)
        fill(132)
    else:
        background(103)
        rect(30, 30, 80, 80)
        fill(0)
        
