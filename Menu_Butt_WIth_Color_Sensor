from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Stop, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait, hub_menu

color_sensor = ColorSensor(Port.D)
while True:
    if color_sensor.reflection() < 10:
        selected = hub_menu('A', 'B', 'C')
        break