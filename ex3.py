import turtle
import random as rnd

my_turtle = turtle.Turtle()
my_win = turtle.Screen()

def tree(branch_len, t):  
    if branch_len > 5:
        t.color('green')
        t.forward(branch_len)
        t.right(rnd.randrange(15,25))
        tree(branch_len - rnd.randrange(20, 30), t)
        t.width(t.width() - 1)
        t.left(40)
        tree(branch_len - rnd.randrange(20, 30), t)
        t.right(rnd.randrange(15, 25))
        t.backward(branch_len)
        t.color('brown')
        t.width(t.width() + 1)



def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.width(10)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    tree(75, t)
    my_win.exitonclick()

main()
