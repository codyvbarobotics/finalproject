from gpiozero import Robot
from time import sleep

motor = Robot (left=(4,14), right=(24,25))

while True:
  motor.left()
  sleep(5)
  motor.stop()
  sleep(5)
