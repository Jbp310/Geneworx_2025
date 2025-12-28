`from pybricks.hubs import PrimeHub`  
`from pybricks.pupdevices import Motor`  
`from pybricks.parameters import Port, Direction, Stop`  
`from pybricks.robotics import DriveBase`  
`from pybricks.tools import wait`

`The first line tells us to import the hub itself and tells the code which hub you’re using. The second line tells us what electronic parts are connected through wires to the hub. The third line tells the code parameters that will be needed during later code. The fourth line tells the code commands and stuff about coding the robot. The fifth line tells the code tools that will be useful in coding.`   
`hub = PrimeHub()`

`left_motor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)`  
`right_motor = Motor(Port.B, positive_direction=Direction.CLOCKWISE)`

`robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=110)`

`This is code that sets up the robot’s movement. It defines motors, the drivebase, and the robot measurements.`   
`def i2m(inches):`  
    `return inches * 25.4`  
`Turns inches to millimeters.`   
`def gyro_straight(distance, base_speed=300, gain=3.0):`  
    `# Convert mm -> motor degrees (≈ 360° per 56 mm wheel)`  
    `wheel_circ = 56 * 3.1416`  
    `target_angle = distance / wheel_circ * 360`  
    `# Reset sensors`  
    `hub.imu.reset_heading(0)`  
    `left_motor.reset_angle(0)`  
    `right_motor.reset_angle(0)`  
    `while True:`  
        `avg_angle = (abs(left_motor.angle()) + abs(right_motor.angle())) / 2`  
		  
        `if avg_angle >= target_angle:`  
            `break`  
		`if target_angle - avg_angle < 0.1 * target_angle`        
            `gain = 1`

         
        `error = hub.imu.heading()`  
        `if error > 180:`  
            `error -= 360`  
        `elif error < -180:`  
            `error += 360`

`This is the gyro straight function. It moves the robot straight and when not off course it adjusts the robot to be back on course. Using the distance the function first turns distance into the amount of degrees the wheel has to turn. Then it resets the yaw angle and motor (wheel) angles. The next few lines calculate the distance traveled and stop the robot accordingly. It also prevents too much adjustment at the end (leaves the robot in an awkward position). Then it calculates the error. It also makes sure the error is not on a 360 degree scale. It makes it so the highest possible error is 180 and the lowest is -180. This way, 0 is no error and a little error to the left isn’t in the 300s.`   
`if base_speed < 0:`  
            `correction = -error * gain`  
        `else:`  
            `correction = error * gain`    
         
         `# Compute motor speeds`  
           
        `if base_speed >= 0:`  
            `left_speed = base_speed - correction`  
            `right_speed = base_speed + correction`  
        `else:`  
            `left_speed = base_speed + correction`  
            `right_speed = base_speed - correction`

        `left_motor.run(left_speed)`  
        `right_motor.run(right_speed)`  
       

        `wait(10)`

    `left_motor.stop()`  
    `right_motor.stop()`

`The if statements with base_speed then something is just used so the robot can correct correctly when moving backwards. Here we calculate the correction, speed, and we apply it to the motors. After the while loop breaks, the motors stop moving.`

`def gyro_turn(direction, turn_angle=90, max_speed=300, correction=4.0):`

    `hub.imu.reset_heading(0)`  
    `wait(100)`

    `while True:`  
        `current_angle = hub.imu.heading()`  
        `error = turn_angle - abs(current_angle)`

        `# Stop when close enough`  
        `if error <= 1:`  
            `break`

        `# Proportional speed`  
        `speed = max(min(error * correction, max_speed), 80)`  
     
        `if direction == "left":`  
            `left_motor.run(-speed)`  
            `right_motor.run(speed)`  
        `elif direction == "right":`  
            `left_motor.run(speed)`  
            `right_motor.run(-speed)`

        `wait(10)`

    `left_motor.stop()`  
    `right_motor.stop()`  
    `wait(200)`  
`This function turns accurately and won’t stop until the robot is at the right angle. First, we get the yaw, calculate the error, and check if the error is close enough for the robot to stop. Second, we calculate the speed and make sure that the robot doesn’t turn too slow or too fast to minimize inaccurate or slow turns. Third, we apply the speeds to the motors based on the direction. Finally, we stop the motors after the while loop breaks.`  
`option1 = []`  
`direction1 = []`  
`distance1 = []`  
`turn_angle1 = []`  
`correction1 = []`  
`speed1 = []`  
`Here we just set up some empty lists.`   
`def array(option1 ,direction1, distance1,turn_angle1,correction1,speed1):`  
    `#option 1 is straight and option 2 is turn`  
     
    `array_length = len(option1)`  
    `x = 0`  
    `while True:`  
        `if array_length == x :`  
            `break`  
        `direction= direction1[x]`  
        `option = option1[x]`  
        `distance = distance1[x]`  
        `turn_angle = turn_angle1[x]`  
        `correction = correction1[x]`  
        `speed = speed1[x]`  
        `if option == 1:`  
            `gyro_straight(distance,speed,correction)`  
        `elif option == 2:`  
        	   `gyro_turn (direction,turn_angle,speed,correction)`  
        `else :`  
            `print("Option is incorrect or missing")`  
        `x = x + 1`  
`First we check the array length by looking at the amount of items in option1. Then, we take values from each list. The x item will be taken (in python logic 0 would be the first item and 1 would be the 2nd). After that, according to the value taken from option1, we will apply the other values to their respective functions. Finally, we will add 1 to x and take the next value from each list or the value will be equal to the array length and the loop will break.`   
`array(`  
`option1 =    [1,1,2],`  
`direction1 = [0,0, "left"],`  
`distance1 =  [500,500,0],`  
`turn_angle1 =[0,0,90],`  
`correction1 =[1,1,3],`  
`speed1=      [800,-800, 800],`  
`)`  
`This is an example of someone calling the array. You should call it with keywords so you actually know which list is which. Each line is a list and they are separated by commas. This is just calling a function across multiple lines for organization.`