def turnleft(direction):
    left={(0,1):(-1,0), (-1,0):(0,-1),(0,-1):(1,0),(1,0):(0,1)}
    try:
        direction=left[direction]
    except:
        raise ValueError("Not a valid direction")
    return direction
def turnright(direction):
    right={(-1,0):(0,1),(0,-1):(-1,0),(1,0):(0,-1),(0,1):(1,0)}
    try:
        direction=right[direction]
    except:
        raise ValueError("Not a valid direction")
    return direction
def move(coord,direction):
    coord[0]+=direction[0]
    coord[1]+=direction[1]
    return coord
def add(coord,system,value=0):
    if (coord[0] not in system):
        system[coord[0]]={}
    system[coord[0]][coord[1]]=value
    return system
def moveant(system,direction,position,command):
    system[position[0]][position[1]]=int(not system[position[0]][position[1]])
    if (command=="c"):
        if (system[position[0]][position[1]]==0):
            command="l"
        else:
            command="r"
    if (command=="l"):
        direction=turnleft(direction)
    if (command=="r"):
        direction=turnright(direction)
    position=move(position,direction)
    system=add(position,system,0)
    return [system,direction,position]
def langton(commands,system={0:{0:0}},direction=(1,0),position=[0,0]):
    commands=list(commands)
    #direction=(1,0)
    #position=[0,0]
    for i in commands:
        result=moveant(system,direction,position,i)
        system=result[0]
        direction=result[1]
        position=result[2]
    return [system,direction,position]
