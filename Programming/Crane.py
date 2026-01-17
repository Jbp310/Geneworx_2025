from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

left = Motor(Port.A, positive_direction = Direction.COUNTERCLOCKWISE)
right = Motor(Port.B, positive_direction = Direction.CLOCKWISE)
move = DriveBase(left, right, 54, 65)

def agl(degres):
    turn = (degres * 1.706)
    return int(turn)
def i2m(inches) :
    milimeters = (inches * 25.4)
    return int(milimeters)

x = 0

move.straight(i2m(10))
move.turn(agl(-78))
move.straight(i2m(25))
move.turn(agl(-47))
move.straight(i2m(-3))
move.turn(agl(-45))
while x < 9:
    move.turn(agl(45))
    move.turn(agl(-45))
    move.turn(agl(45))
    move.turn(agl(-45))
    move.straight(i2m(-1))
    x = x + 1