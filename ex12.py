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


def draw_rectangle(turt, color, position, size):
    turt.up()
    turt.fillcolor(color)
    turt.goto(position[0][1])
    turt.down()
    turt.forward(size[0])
    turt.begin_fill()
    turt.left(90)
    turt.forward(size[1])
    turt.left(90)
    turt.forward(size[0])
    turt.left(90)
    turt.forward(size[1])
    turt.end_fill()


def main():
    my_win = t.Screen()
    big = t.Turtle()
    draw_rectangle(big, 'blue', pos11, big)
    middle = t.Turtle()
    draw_rectangle(middle, 'yellow', pos12, mid)
    small = t.Turtle()
    draw_rectangle(small, 'green', pos13, small)
    my_win.exitonclick()

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

###########size

big = [30, 20]
mid = [25, 15]
small = [20, 10]
####################


move_tower(3, "A", "B", "C")
main()

