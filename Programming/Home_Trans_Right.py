from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from Gyro_Straight import *
from pybricks.parameters import Axis

hub = PrimeHub()


hub.imu.reset_heading(0)
hub.speaker.beep(500,100)
orientation = hub.imu.gyro(Axis.Z)

wait(3000)
print(orientation)
if(orientation < 0):
    gyro_straight(400, 800)
    gyro_turn('right',45)
    gyro_straight(175,800)
    gyro_turn('left',45)
    gyro_straight(30000,800)
    print("facing left")

else:
    gyro_straight(400, 800)
    gyro_turn('left',45)
    gyro_straight(175,800)
    gyro_turn('right',45)
    gyro_straight(30000,800)
    print("facing right")