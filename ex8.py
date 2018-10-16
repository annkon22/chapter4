###################################################
###########       Koch Snowflake      #############
###################################################



import turtle 

def koch(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        koch(t, length/3, depth - 1)
        t.right(60)  
        koch(t, length/3, depth -1)
        t.left(120)
        koch(t, length/3, depth - 1)
        t.right(60)
        koch(t, length/3, depth - 1)


def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.color("sky blue")
    t.width(3)
    t.speed(30)
    t.length = 500
    t.depth = 4
    koch(t, 400, 5)
    my_win.exitonclick()

main()
