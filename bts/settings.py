#settings to run BTS
#all just python variables

#========= Notes ===========
#BTS runs in two different ways, this is a nightmare for the uninitiated
#absolute millimeter positions to run the XY table
#and pixel heights to run the collision detection/placing
#0.3528mm height per point size 72pt = 1in = 25.4mm
#pillow uses pixel height (documentation lies) for font size
#the board is created in memory using the measurements and
#pixel density figures
#this figure is represented in millimeters from the upper right
#to check for serial in console: ls -ltr /dev|grep -i ttyUSB

dataBaseFile = "dataBase.db"
ttfFontFile = "bts/fonts/Avenir-Medium-09.ttf"
gCodeFontFile = "bts/fonts/Avenir-Medium-GCode.txt"
centerMaskPNG = "bts/center.png"

wsLogFile = "wsLog.txt"
gCodeFile = "output.txt"

pixelDensity = 12 #pix/mm
boardHeightmm = 950 #mm
boardLengthmm = 410 #mm
borderOffset = 10 #mm

gCodeDecimals = 4
xPosCalmm = 0 
yPosCalmm = 0 
#fontSizeCurve = 0.004
fontSizeCurve = 0.005
fontMaxPixHeight = 240 #font size is in pixels
fontMinPixHeight = 60
collisionPixelRadius = 20 #yeah so this is actually wrong, it's int(font size/collision) so, that's bad

pubSubUserId = "761550336"

#not in there yet, should it fail or lower font size
failsToExit = 700

bigRedButtonPin = 6
bufferGRBL = 128
serialSpeed = 115200
serialAddy = '/dev/ttyUSB0'

#============= gCommands ============
homing = 'G0 X0 Y0\n' #grbl home
clearErr = '$X\n'
units = 'G21\n' #units in mm
dist_mode = 'G90\n' #absolute posns
start_cmd = 'M4 S1000\n'
feed_rate = 'F3000.0000\n'

stop_cmd = 'G0 X0 Y0\nM3\nM5\n'
pulloff_pos = 'G0 X0 Y0\n'

pwr_cycle = '\x18\n'

#=========== statuses =============
nameEntered = 0
namePlaced = 1
nameGcode = 2
nameBurnt = 3