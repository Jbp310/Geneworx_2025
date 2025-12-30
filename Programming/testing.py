from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait



    
hub = PrimeHub()
attachment_motor = Motor(Port.F, positive_direction=Direction.CLOCKWISE)
left_motor = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, positive_direction=Direction.CLOCKWISE)
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=110)
def angle_adjust(angle):
    if angle > 0:
        return angle - angle/90 * 15
    elif angle < 0:
        return angle+ angle/90 * 15
robot.straight(400)
robot.turn(90)
