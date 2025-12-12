from simulator import robot, FORWARD, BACKWARD, STOP
import pygame


def stop_robot():
    robot.motors(STOP, STOP, 0)
def move_forward(seconds):
    """This function does makes the robot move forwaard for x seconds. """
    robot.motors(FORWARD, FORWARD, seconds)
def move_backward(seconds):
    """this makes the robot move backward for x seconds"""
    robot.motors(BACKWARD, BACKWARD, seconds)
def turn_right(seconds):
    """this makes the robot turn right becase the left wheel moves forward and right wheel makes back so ti turns right"""
    robot.motors(FORWARD, BACKWARD, seconds)
def turn_left(seconds):
    """opposite of turns right"""
    robot.motors(BACKWARD, FORWARD, seconds)
def keep_safe():
    left = robot.left_sonar()
    right = robot.right_sonar()
    if left < 20 or right < 20:
        stop_robot()
        move_backward(1)
TURN_90 = 1.53
STROKE_TIME = 7
SPACING_TIME = 4
def turn_90_right():
    turn_right(TURN_90)
    stop_robot()
def turn_90_left():
    turn_left(TURN_90)
    stop_robot()

def draw_M():
    turn_90_left()
    move_forward(STROKE_TIME)
    stop_robot()
    move_backward(STROKE_TIME)
    stop_robot()
    turn_90_right()
    move_forward(SPACING_TIME)
    stop_robot()
    turn_90_left()
    move_forward(STROKE_TIME)
    stop_robot()
    move_backward(STROKE_TIME)
    stop_robot()
    turn_90_right()
    move_forward(SPACING_TIME)
    stop_robot()
    turn_90_left()
    move_forward(STROKE_TIME)
    stop_robot()
    move_backward(STROKE_TIME)
    stop_robot()
    
            

def draw_spin():
    turn_right(1)
    move_forward(0.5)
    turn_left(1)
    stop_robot()

def main():
    
    loops_choice = input("Choose number of loops (1, 2): ").strip().lower()
    if loops_choice == "1":
        max_loops = 1
    elif loops_choice == "2":
        max_loops = 2
    else:
        max_loops = 2

    spin_choice = input("Do you want to spin before drawing M? (yes, no): ").strip().lower()
    if spin_choice == "yes":
        draw_spin()
    if spin_choice == "no":
        print("Skipping spin")
    else: 
        draw_spin()
    while True:
        draw_M()
        loops = 0
        loops+=1
        

if __name__ == "__main__":
    main()

robot.exit()

    





