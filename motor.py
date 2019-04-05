from gpiozero import Motor
from time import sleep

motor = Motor (forward=24, backward=25)

while True:
  motor.forward()
  sleep(5)
  motor.backward()
  sleep(5)
