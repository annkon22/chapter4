def rev_list(lst):
    if len(lst) == 0:
        return lst
    else:
        return [lst[-1]] + rev_list(lst[:-1])



my_lst = input('Provide a list of numbers: ').split()
print(rev_list(my_lst))