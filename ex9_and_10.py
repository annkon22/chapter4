##############################################################
##Write a program to solve the following problem:   ##########
# You have two jugs: a 4-gallon jug and a 3-gallon jug.      #
# Neither of the jugs have markings on them. There is a pump #
# that can be used to ﬁll the jugs with water. How can you   #
# get exactly two gallons of water in the 4-gallon jug?      #

def fill_jug(filled, jug1, jug2):

    if (filled / jug1) == 0.5:
        print("The jug is filled with 2 litres of water")
        return
    else: fill_jug(filled + .5, jug1, jug2)

my_jug1 = 4
my_jug2 = 3
my_fill = 0



#fill_jug(my_fill, my_jug1, my_jug2)

## Generalized:

def fill_jug1(filled, jug1, jug2, level):

    if (filled / jug1) == level:
        print(str.format("The jug is filled with {0} litres of water", my_lev))
        return
    else: fill_jug1(filled + .5, jug1, jug2, level)

my_jug3 = 4
my_jug4 = 3
my_f = 0
my_lev = int(input("How many litres should be in a jug?"))

fill_jug1(my_f, my_jug1, my_jug2, my_lev)
