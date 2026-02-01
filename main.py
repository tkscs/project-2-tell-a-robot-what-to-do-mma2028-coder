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

def too_close():
    left = robot.left_sonar()
    right = robot.right_sonar()
    return left < SAFE_DISTANCE or right < SAFE_DISTANCE

def safe_forward(total_seconds):
     elapsed = 0.0
     while elapsed < total_seconds:
          if too_close():
               stop_robot()
               move_backward(0.5)
               stop_robot()
               return False
          robot.motors(FORWARD, FORWARD, STEP_TIME)
          elapsed += STEP_TIME
          stop_robot()
     return True
SAFE_DISTANCE = 20
STEP_TIME = 0.2
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
    safe_forward(STROKE_TIME)
    safe_forward(STROKE_TIME)
    stop_robot()

    move_backward(STROKE_TIME)
    stop_robot()
    turn_90_right()
    safe_forward(SPACING_TIME)
    stop_robot()
    turn_90_left()
    safe_forward(STROKE_TIME)
    stop_robot()
    move_backward(STROKE_TIME)
    stop_robot()
    turn_90_right()
    safe_forward(SPACING_TIME)
    stop_robot()
    turn_90_left()
    safe_forward(STROKE_TIME)
    stop_robot()
    move_backward(STROKE_TIME)
    stop_robot()
    
            

def draw_spin():
    turn_right(1)
    safe_forward(0.5)
    turn_left(1)
    stop_robot()

def main():
    
    print("robot controller started, select type 'exit' to quit")
    loops_choice = input("Choose number of loops (1, 2, 3, inf): ").strip().lower()
    if loops_choice == "1" or loops_choice == "2" or loops_choice == "3":
        max_loops = int(loops_choice)
    elif loops_choice == "inf":
        max_loops = None
    else:
        print("Invalid, default 1 loop")
        max_loops = 1

    spin_choice = input("Do you want to spin? (yes, no, twice): ").strip().lower()
    if spin_choice == "yes":
        draw_spin()
    elif spin_choice == "no":
        print("Skipping spin")
    elif spin_choice == "twice":
        draw_spin()
        draw_spin()
    loops_done = 0
    
    while True:
        command = input("Command (m, spin, forward, back, left, right, exit)")
        if command == "m":
            draw_M()
            loops_done += 1
        elif command == "spin":
            draw_spin()
        elif command == "forward":
            move_forward(1)
        elif command == "back":
            move_backward(1)
        elif command == "left":
            turn_left(0.5)
            stop_robot()
        elif command == "right":
            turn_right(0.5)
            stop_robot()
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()
    robot.exit()



    





