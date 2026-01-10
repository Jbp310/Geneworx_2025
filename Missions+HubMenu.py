from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, hub_menu
from Mission_Code import mission_code_left_side_1,mission_code_left_side_2, mission_code_left_side_3,mission_code_right_side_1
#MAKE SURE IN THE FILE YOU'RE IMPORTING ONLY DEFINES FUNCTIONS, IMPORTING WILL ACtuaLLY RUN THE WHOLE FILE BEFORE RUNNING THE CODE ON THIS FILE
selected = None
selected = hub_menu("A", "B", "C", "D", "E")
while selected != None:
    if selected == "A":
        mission_code_right_side_1()
        break
    elif selected == "B":
        #functions not yet implemented
        home_transfer()
        break
    elif selected == "C":
        mission_code_left_side_1()
        break
    elif selected == "D":
        mission_code_left_side_2()
        break
    elif selected == "E":
        mission_code_left_side_3()
        break
        
