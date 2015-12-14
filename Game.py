from sys import exit

def forest():
    print "Success, at least for the moment. You have narrowly escaped the guards."
    print "As you look around you seem to be on top of a mountain range."
    print "You can begin your descent or you can rest for the night."

  


def ladder_room():
    print "In the middle of the room you see a ladder. It is lightly guarded."
    print "Will you attempt to FIGHT the guard or CLIMB the ladder?"

    next = raw_input("> ")
    if "fight" in next:
        decision = str(next)
        print "You wrestle the guard to the ground, and you take his armor and sword"
        print "You climb the ladder after your endevour"
        forest()
    elif "climb" in next:
        decision = str(next)
        print "You manage to sneak past the guard and climb the ladder"
        forest()

def armory():
    print "You find over 10 heavily armed guards in this room"
    print "You are captured, and put back in your cell.\n"
    cell()


def hallway():
    print "You are our of your cell and in a hallway"
    print "There are two ways you can go, LEFT or RIGHT"
    print "Choose carefully!"

    next = raw_input("> ")
    if "left" in next:
        ladder_room()
    elif "right" in next:
        armory()
    else:
        dead("You wasted too much time and guards have found you")

def dead(why):
    print why, "Good Job!"
    exit(0)


def guard():
    print "You see a figure guarding your cell door"
    print "You notice that he has a key"
    print "Do you try and get the key? (Y/N)"

    next = raw_input("> ")
    if "yes" in next:
        print "You get the key, the guard doesn't notice"
        hallway()
    else:
        dead("You are too scared, and die in your cell")

def cell():
    print "You find yourself in a cell"
    print "You need to get OUT before you are executed"

    next = raw_input("> ")
    if "out" in next:
        guard()
    else:
        dead("The guard leaves, and never returns. Leaving you to die in your cell.")
    

cell()

