import random
obs = []


def genOBs():
    """
    generates 1 to 10 obstacles and then is added to A Tuple
    """
    global obs
    noOBS = random.randint(1,10)
    for i in range(noOBS):
        X = random.randint(-100,100)
        Y = random.randint(-200,200)
        co = (X,Y)
        obs.append(co)
    return obs

def is_position_blocked(new_x, new_y) :
    """
    checks the robots current postion and compares it to
    where it wants to go then
    checks if any of the obstacles matches the cords
    
    """
    for i in range(len(obs)):
        block = obs[i]
        if block[0] == new_x and new_y == block[1]:
            return True


def path_is_blocked(position_x,position_y,new_x, new_y):
    """
    creates and square obstacle ,checks if the robot
    lands in it
    """
    for i in range(len(obs)):
        blocked = obs[i]
        min_x = blocked[0]
        max_x = blocked[0]+4
        min_y = blocked[1]
        max_y = blocked[1]+4
        #####################
        if min_x < position_x < max_x and min_y < position_y < max_y:
            return True
        else :
            return False


def is_path_blocked(position_x,position_y,new_x,new_y):
    """
    checks if any of the obstuctions are inbetween
    the current and new cord
    if it is itll send back a bool
    """
    for i in range(len(obs)):
        blocked = obs[i]
        min_x = blocked[0]
        max_x = blocked[0]+4
        min_y = blocked[1]
        max_y = blocked[1]+4

        if position_x == new_x:
            if position_x < new_x :
                position_x,new_x = new_x,position_x
            for j in range(position_x,new_x+1):
                if min_x <= j <= max_x :
                    return True
        
        elif position_y== new_y :
            if position_y < new_y:
                position_y,new_y = new_y,position_y 
            for j in range(position_y ,new_y +1) :
                if min_y <= j <= max_y  :
                    return True

genOBs()
