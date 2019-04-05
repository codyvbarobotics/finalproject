from gpiozero import Robot
from time import sleep

robot = Robot(left=(4, 17), right=(24, 25))

for i in range(4):
  robot.forward()
  sleep(10)
  robot.backward()
  sleep(1)
