from gpiozero import Motor
from gpiozero import DistanceSensor
from time import sleep
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
from gpiozero import RGBLED
from colorzero import Color
motor_L = Motor (forward=17, backward=27)
motor_R = Motor (forward=22, backward=23)
sensor = DistanceSensor (echo=5, trigger=20)

#Separately Define Robot Movements. def moveForward(): print ("Moving Forward")
forStr = "Moving Forward \n ^_^"
backStr = "Backing up \n ^_^"
stopStr = "Stopped \n 0_0"
rightStr = "Reversing Right \n -_^"
leftStr = "Reversing Left \n ^_-"

def moveForward():
motor_L.forward(speed = 0.4)
motor_R.forward(speed = 0.4)
print("Moving Forward")

def moveBackward():
motor_L.backward(speed = 0.3)
motor_R.backward(speed = 0.3)
print("Moving Backward")

def robotStop():
motor_L.forward(speed = 0)
motor_R.backward(speed = 0)
print("Robot Stop")

def moveBackwardRight():
motor_L.backward(speed = 0.3)
motor_R.backward(speed = 0.6)
print("Moving Backward Right")

def moveBackwardLeft():
motor_L.backward(speed = 0.6)
motor_R.backward(speed = 0.3)
print ("Moving Backward Left")

i2c = board.I2C()
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)
small_font = ImageFont.truetype('FreeSans.ttf', 12)
large_font = ImageFont.truetype('FreeSans.ttf', 18)
disp.fill(0)
disp.show()
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
def display_message(top_line, line_2):
draw.rectangle((0,0,width,height), outline=0, fill=0)
draw.text((0, 0), top_line, font=large_font, fill=255)
draw.text((0, 50), line_2, font=small_font, fill=255)
disp.image(image)
disp.show()

rgb_led = RGBLED(12, 6, 13)
red = 0
green = 0
blue = 0
def toGreen():
rgb_led.off()
rgb_led.on()
rgb_led.color = Color(0, 255, 0)
def toRed():
rgb_led.off()
rgb_led.on()
rgb_led.color = Color(255, 0, 0)
def toYellow():
rgb_led.off()
rgb_led.on()
rgb_led.color = Color(255, 48, 0)

count=0

while True:
  dist_cm = sensor.distance * 100
  flag=0
  distStr = "distance={:.1f}".format(dist_cm)
  print(distStr)
  if dist_cm <= 20:
    count=count+1
    toRed()
    robotStop()
    display_message(stopStr, distStr)
    sleep(0.1)
    toYellow()
    rgb_led.blink(0.5, 0.5, on_color = (255, 48, 0), background = True)
    moveBackward()
    display_message(backStr, distStr)
    sleep(0.1)
  if (count%3 == 1) & (flag == 0):
    moveBackwardRight()
    display_message(rightStr, distStr)
    sleep(0.1)
    flag = 1
  else:
    moveBackwardLeft()
    display_message(leftStr, distStr)
    flag = 0
    sleep(0.1)
else:
  moveForward()
  toGreen()
  moveForward()
  display_message(forStr, distStr)
  flag = 0
