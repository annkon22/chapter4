#calculaing the sm of a list of numbers

def list_sum(num_list):
    the_sum = 0 
    for i in num_list:
        the_sum += i
    return the_sum


def list_sum1(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])


print(list_sum1([0, 1]))        
print(list_sum([1, 3, 5, 6]))    

#the three laws of recursion:
# A recursicve algorithm must have a base case
# A recursive algorithm must change its state and move toward the base case
# A recursive algorithm must call itself, recursively


