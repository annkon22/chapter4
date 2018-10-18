def move_(left_side, c, m):
    step = 0
    go_boat = []


    go_boat.append('c')
    go_boat.append('m')
    
    left_side.remove('c')
    left_side.remove('m')
    step +=1
    if left_side == 1:
        return
    else:
        if step % 2 != 0:
            move_(l_side, c, m-1)
        else:
            move_(l_side, c-1, m)


l_side = ['c' for _ in range(3)]
l_side += ['m' for _ in range(3)]

print(move_(l_side, 3, 3))







      
#class Cannibal:

#    def __init__(self):       self.cannibal = c

#class Missioner:
    #def __init__(self):        self.missioner = m




