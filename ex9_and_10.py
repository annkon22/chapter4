##############################################################
##Write a program to solve the following problem:   ##########
# You have two jugs: a 4-gallon jug and a 3-gallon jug.      #
# Neither of the jugs have markings on them. There is a pump #
# that can be used to ﬁll the jugs with water. How can you   #
# get exactly two gallons of water in the 4-gallon jug?      #

def fill_jug(jug1, jug2, jug3):
    jug1 += 4
    jug2 = jug1 - 1

    jug3 += jug1 - jug2
    jug1 = 0
    jug2 = 0
    if jug3 == 2:
        print("The jug is filled with 2 litres of water")
        return
    else:
        fill_jug(jug1, jug2, jug3)

my_jug1 = 0
my_jug2 = 0
damp_jug = 0

fill_jug(my_jug1, my_jug2, damp_jug)

## Generalized:

def fill_jug1(jug1, j1, jug2, j2, jug3, lev):

    jug1 += j1
    jug2 = jug1 - (j1 - j2)
    if jug1 >= jug2:
        jug3 += jug1 - jug2
    else:
        jug3 += jug2-jug1
    jug1 = 0
    jug2 = 0
    if jug3 == lev:
        print(str.format("The jug is filled with {0} litres of water", my_lev))
        return
    elif jug3 < lev:
        fill_jug1(jugy1, my_j1, jugy2, my_j2, st_jug, my_lev)
    else:
        print("Impossible to fill the jug")
        return
jugy1 = 0
jugy2 = 0
my_j1 = int(input("How many litres in the 1 jug? "))
my_j2 = int(input("How many litres in the 2 jug? "))
st_jug = 0
my_lev = int(input("How many litres should be in a jug?"))

fill_jug1(jugy1, my_j1, jugy2, my_j2, st_jug, my_lev)

