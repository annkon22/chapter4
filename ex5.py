def fib(num):
    fib_lst = [1, 1]
    for i in range(len(fib_lst)+1):
        fib = fib_lst[i] + fib_lst[i+1]
        fib_lst.append(fib)
       
        if len(fib_lst) == num:
            return fib
        else:
            return fib(num)





        

my_num = int(input("How many numbers? "))
print(fib(my_num))
