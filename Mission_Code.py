from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from gyro_functions import array, gyro_reset_to_straight, gyro_turn, gyro_straight
from pybricks.parameters import Axis
hub = PrimeHub()
def mission_code_right_side_1():
      array(
    option1=     [],
    direction1 = [],
    distance1 =  [],
    turn_angle1 =[],
    correction1= [],
    speed1 =     [],
    )  
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
def mission_code_right_side_1():
    array(
    option1 =    [1,3,3,3,3,3,3,2,1,3,1],
    direction1 = [0,0,0,0,0,0,0,"left",0,0,0], 
    distance1 =  [350,0,0,0,0,0,0,0,190,0,500],
    turn_angle1 =[0,-690,690,-690,690,-690,900,48,0,-900,0],
    correction1 =[3,0,0,0,0,0,0,3,3,0,3],
    speed1=      [800,2500,1600,1600,1600,1600,1600,2000,800,1600,-800],
    )



def home_transfer_left():
    gyro_straight(400, 800)
    gyro_turn('right',45)
    gyro_straight(175,800)
    gyro_turn('left',45)
    gyro_straight(30000,800)
    print("facing left")
def home_transfer_right():
    gyro_straight(400, 800)
    gyro_turn('left',45)
    gyro_straight(175,800)
    gyro_turn('right',45)
    gyro_straight(30000,800)
    print("facing right")