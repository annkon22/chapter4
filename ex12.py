#Modify the Tower of Hanoi program using turtle graphics to animate the movement of the disks. 
#Hint: You can make multiple turtles and have them shaped like rectangles.

import turtle as t

def move_tower(height, from_pole, to_pole, with_pole):
    if height >=1:
        move_tower(height - 1, from_pole, with_pole, to_pole) 
        move_disk(from_pole, to_pole)     
        move_tower(height - 1, with_pole, to_pole, from_pole)   

def move_disk(fp, tp):
    print("moving disk from ", fp, "to", tp)

def move_turtle(turt, position):
        print("The", turt, "goes to", position)

def bigger(turt1, turt2):
        return turt1.shapesize() > turt2.shapesize()
                



def moved(height,pole):
    if height[pole] == 3:
        return True

def main():
    my_win = t.Screen()

    big = t.Turtle()
    big.shape('square')
    big.shapesize(50)

    mid = t.Turtle()
    mid.shape('square')
    mid.shapesize(30)



    small = t.Turtle()
    small.shape('square')
    small.shapesize(15)

    list_turts = [big, mid, small]
    
    my_win.exitonclick()

poleA = []
poleB = []
poleC = []
        
poles = [poleA, poleB, poleC]

while not moved:
    

    if len(poleA) == 3 and len(poleB) == 0:
        move_disk(poleA, poleB)
        len(poleA) -= 1
        len(poleB) += 1
        move_turtle(list_turts[2], pos21)
        list_turts[2].goto(pos21)
    if len(poleA) == 2  and len(poleC) == 1:
            if poleA[2] not bigger poleC:
                move_turtle(poleA[2], pos32)











#######positions
pos11 = [0, 0]
pos12 = [0, 50]
pos13 = [0, 90]

pos21 = [40, 0]
pos22 = [40, 50]
pos23 = [40, 90]

pos31 = [80, 0]
pos32 = [80, 50]
pos33 = [80, 90]

################


move_tower(3, "A", "B", "C")
main()

