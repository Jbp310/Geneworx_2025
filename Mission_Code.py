from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from gyro_functions import array, gyro_reset_to_straight

def mission_code_left_side_1():
    array(
    option1=     [1,3,1,3],
    direction1 = [0,0,0,0],
    distance1 =  [350,0,500,0],
    turn_angle1 =[0,-200,0,210],
    correction1= [0.2,0,0.2,0],
    speed1 =     [800,1000,-800,800],
    )
def mission_code_left_side_2():
    array(
    option1=     [1,1],
    direction1 = [0,0],
    distance1 =  [1000,1000],
    turn_angle1 =[0,0],
    correction1= [3,3],
    speed1 =     [800,-800],
    )
def mission_code_left_side_3():
    array(
    option1=     [1,2,1,1,3,1,2,1,1,2,1],
    direction1 = [0,"left",0,0,0,0,"left",0,0,"right",0],
    distance1 =  [650,0,300,300,0,250,0,400,200,0,1000],
    turn_angle1 =[0,35,0,0,300,0,20,0,0,80,0],
    correction1= [3,3,3,3,0,3,3,3,3,3,5],
    speed1 =     [800,2000,-800,800,800,-800,2000,800,-800,800,-1000],
    )
