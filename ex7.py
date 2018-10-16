#Using the turtle graphics module, write a recursive
#program to display a Hilbert curve


###############################################
##########      HILBERT CURVE       ###########
import turtle
size = 10
def main():
    t = turtle.Turtle()
    my_wd = turtle.Screen()
    hilbert(t, 5, 90)
    my_wd.exitonclick()




def hilbert(t, level, angle):
    if level == 0:
        return
    t.color('Blue')
    t.width(5)
    t.speed(2)

    t.right(angle)
    hilbert(t, level - 1, - angle)
    t.forward(size)
    t.left(angle)
    hilbert(t, level - 1, angle)
    t.forward(size)
    hilbert(t, level - 1, angle)
    t.left(angle)
    t.forward(size)
    hilbert(t, level - 1, - angle)
    t.right(angle)

main()





