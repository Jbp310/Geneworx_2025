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

move.straight(i2m(8))
move.turn(agl(-92))
move.straight(i2m(28.5))
move.turn(agl(-30))
while x < 9:
    move.straight(i2m(-2))
    move.straight(i2m(2))
    x = x + 1