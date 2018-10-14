def rev_list(lst):
    return [lst[-1]] + rev_list(lst[:-1]) if lst else []



my_lst = input('Provide a list of numbers: ').split()
print(rev_list(my_lst))
