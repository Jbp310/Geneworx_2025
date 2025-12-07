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
    turn = (degres * 1.234)
    return int(turn)
def i2m(inches) :
    milimeters = (inches * 25.4)
    return int(milimeters)

move.straight(i2m(3))
move.turn(agl(-92))
move.straight(i2m(18))
move.turn(agl(15))
move.straight(i2m(2))
move.turn(agl(-15))