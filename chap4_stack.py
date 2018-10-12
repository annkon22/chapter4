

import module_stack as stack

r_stack = stack.Stack()

def to_str(n, base):
    convert_str = '013456789ABCDEF'
    while n > 0:
        if n < base:
            r_stack.push(convert_str[n])
        else:
            r_stack.push(convert_str[n % base])
        n = n // base

    res = ''
    while not r_stack.is_empty():
        res = res + str(r_stack.pop())
    return res
print(to_str(10, 2))
    