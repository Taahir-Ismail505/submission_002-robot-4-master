import turtle
import sys
sys.path.append('.')
sys.path.append('./world')
import obstacles

global cord
global obstacles_flag
obstacle_flag = False

cords = []
cords = obstacles.obs
################################################

wn = turtle.Screen() #actaul turtle
wn.title("Handling keypresses!") 
tess = turtle.Turtle()
tess.shape('turtle')
tess.setheading(90)
tess.penup()
pos = list(tess.position())

################################################
shape = turtle.Turtle() #creates the shape for the boarder 
shape.penup()
shape.setpos(100,-200)
shape.hideturtle()
shape.pendown()
shape.pencolor('red')
shape.pensize(3)
shape.speed(5)

for i in range(2):
    shape.left(90)
    shape.forward(400)
    shape.left(90)
    shape.forward(200)
shape.penup()

################################################
def getOBs() :
    for i in range(len(cords)):
        cord = cords[i]
        shape.goto(cord[0],cord[1])
        for i in range(4):
            shape.pendown()
            shape.forward(4)
            shape.left(90)
            shape.penup()

################################################
position_x = 0
position_y = 0
current_direction_index = 0
directions = ['forward', 'right', 'back', 'left']

min_y, max_y = -200, 200
min_x, max_x = -100, 100
################################################
def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """
    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps):
    global obstacle_flag
    obstacle_flag = False
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    checks  obstacles to see if it comes back true
    """
    global position_x, position_y
    
    new_x = position_x
    new_y = position_y
    
    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if obstacles.is_path_blocked(position_x,position_y,new_x,new_y):
        obstacle_flag = True
        return False

    if obstacles.is_position_blocked(new_x, new_y):
        obstacle_flag = True
        return False
    
    elif is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    else: 
        return False


def do_forward(robot_name, steps):
    global obstacle_flag
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    and checks if an obstacle is found
    """
    global pos
    # pos = tess.position()
    if update_position(steps) == True :
        tess.forward(steps)
        return True,' > '+robot_name+' moved forward by '+str(steps)+' steps.'
        
    else:
        if obstacle_flag == True :
            return True , ''+robot_name+': Sorry, there is an obstacle in the way.'
        else :
            return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    and checks if an obstacle is found
    """
    global pos
    if update_position(-steps):
        tess.back(steps)
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    else:
        if obstacle_flag == True :
            return True , ''+robot_name+': Sorry, there is an obstacle in the way.'
        else :
            return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index
    tess.right(90)
    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0
    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index
    tess.right(270)
    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3

    return True, ' > '+robot_name+' turned left.'


def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """
    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)


getOBs()