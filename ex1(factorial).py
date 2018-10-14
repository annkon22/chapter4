#Write a recursive function to compute the factorial of 
#a number


def fact(lst):
    if len(lst) == 1:
        return lst[0] 
    else:
        return lst[0] * fact(lst[1:])

my_top = int(input('Provide a top boundary: '))
my_fact_lst = []
for i in range(my_top, 0, -1):
        my_fact_lst.append(i)
    
print(fact(my_fact_lst))