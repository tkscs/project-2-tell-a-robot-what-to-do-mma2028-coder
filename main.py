from simulator import robot, FORWARD, BACKWARD, STOP
import pygame
#* [ ] robot moves - done
#* [ ] robot does not crash into the walls of the box - done
#* [ ] at least 5 calls to input - done
#* [ ] at least 5 functions
#* [ ] at least 2 functions have at least one parameter - done
#* [ ] at least 2 functions have return values and at least one call to the function is assigned to a variable
#* [ ] each motor moves at least once
#* [ ] the robot's movement changes based on at least 5 readings of the sonar sensors
#* [ ] use at least 1 while loop OR recursive function call
#* [ ] at least one command (user input) causes the robot to move autonomously for at least 20 seconds

def move_forward(seconds):
    """This function does makes the robot move forwaard for x seconds. """
    robot.motors(FORWARD, FORWARD, seconds)
def turn_right(seconds):
    """this makes the robot turn right becase the left wheel moves forward and right wheel makes back so ti turns right"""
    robot.motors(FORWARD, BACKWARD, seconds)
def turn_left(seconds):
    """opposite of turns right"""
    robot.motors(BACKWARD, FORWARD, seconds)
def avoid_obstacle():
    """read left sonar to see if you will hit a wall , if you will hit it turn right, if not then keep moving forward."""
    distance = robot.left_sonar()
    if distance < 5:
       robot(BACKWARD, BACKWARD, 1)
       turn_right(1)
    else:
       move_forward(1)
while True:
    mode = input("Choose mode(Manual, Auto, Exit): ")
    if mode == "Manual":
        command = input("Enter command(forward, backward, left, right, stop): ")
        if command == "Forward":
            move_forward(1)
        elif command == "Backward":
            robot.motors(BACKWARD, BACKWARD, 1)
        elif command == "Left":
            turn_left(1)
        elif command == "Right":
            turn_right(1)
        elif command == "Stop":
            robot.motors(STOP, STOP, 0)
    elif mode == "Auto":
        command - input("Auto?(yes, no)")
        avoid_obstacle()
    elif mode == "Exit":
        command = input("Exit the program?(Yes, No)")
        break
    else:
        print("error")
    

    





