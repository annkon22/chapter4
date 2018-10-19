import module_queue as queue
import copy as copy


def conflicts(side):
    if side[0].size() > side[1].size():
        return True
    
    
def move(left_side, right_side):
    test_lst_left = copy.deepcopy(left_side)
    test_lst_right = copy.deepcopy(right_side)

    test_lst_right.append(test_lst_left[0].pop())
    test_lst_right.append(test_lst_right[1].pop())

    if not conflicts(test_lst_left) and not conflicts(test_lst_right)
        left_side = test_lst_left
        right_side = test_lst_right

    else:
        return "Cannibals ate missioners"


def main(left_side, right_side):
    if left_side[0].size == 0 and left_side[1].size == 0:
        return print("You win!")
        
    else:
        move(left_side, right_side)


my_turn = input("Whom you'll take aboard?").split()

my_can = queue.Queue()
for _ in range(3):
    my_can.enqueue('c')

my_mis = queue.Queue()
for _ in range(3):
    my_mis.enqueue('m')

my_left = []
my_left.append(my_can)
my_left.append(my_mis)

my_right = []
my_right.append(queue.Queue())
my_right.append(queue.Queue())
my_turn = input("Whom you'll take aboard?").split()

print(move(my_left, my_right))


