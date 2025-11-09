from pybricks.tools import hub_menu
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from Pybricks_test import beep
#make a menu to choose letters/numbers
seleted = hub_menu("H", "S", "L")

if seleted == "H":
    beep()