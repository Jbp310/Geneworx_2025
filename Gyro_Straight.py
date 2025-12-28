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
def gyro_reset_to_straight():
    current = hub.imu.heading()
    robot.turn(angle_adjust(-current))
def gyro_straight(distance, base_speed=300, gain=3.0):
    # Convert mm -> motor degrees (≈ 360° per 56 mm wheel)
    wheel_circ = 56 * 3.1416
    target_angle = distance / wheel_circ * 360
    # Reset sensors
    hub.imu.reset_heading(0)
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    while True:
        avg_angle = (abs(left_motor.angle()) + abs(right_motor.angle())) / 2
        if avg_angle >= target_angle:
            gyro_reset()
            break


        
        error = hub.imu.heading()
        if error > 180:
            error -= 360
        elif error < -180:
            error += 360

        # Correct sign for your motor setup
        if base_speed < 0:
            correction = -error * gain
        else:
            correction = error * gain  
       
         # Compute motor speeds
        if base_speed >= 0:
            left_speed = base_speed - correction
            right_speed = base_speed + correction
        else:
            left_speed = base_speed + correction
            right_speed = base_speed - correction

        left_motor.run(left_speed)
        right_motor.run(right_speed)

        wait(10)

    left_motor.stop()
    right_motor.stop()