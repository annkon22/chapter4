def list_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])

print(list_sum([1, 2, 45, 200, 5, 9]))

def to_str(n, base):
    convert_string = '0123456789ABCDEF'
    if n < base:
        return convert_string[n]
    else:
        return to_str(n // base, base) + convert_string[n % base]

print(to_str(10, 2))

#Self check 1
#Write a function that takes a string as a parameter and returns a new string that is the reverse
#of the old string

def rev_string(a_string):
    if len(a_string) == 1:
        return a_string[0]
    else:
        return rev_string(a_string[1:]) + a_string[0]


my_rev = 'apple'
print(rev_string(my_rev))


#########################################################################################
####Write a function that takes a string as a parameter and returns True if the string ##
####is a palindrome                                                                    ##
####For bonus points palindromes can also be frases, but you need to remove            ##
####the spaces and punctuation before checking ##########################################
def pal_check(a_string):
    a_string = a_string.lower()
    check_str = ''
    for i in a_string:
        if i in 'abcdefghijklmnopqrstuvwxyz':
            check_str += i
    
    ok = True
    new_str = ''

    if ok:
        new_str += rev_string(check_str[1:]) + check_str[0]
        if check_str != new_str:
            ok = False

    return ok

print(pal_check('Live not on evil'))
print(pal_check('Reviled did I live, said I, as evil I did deliver'))
print(pal_check('Go hang a salami; Im a lasagna hog'))
print(pal_check('Able was I ere I saw Elba'))
print(pal_check('Kanakanak - a town in Alaska'))
print(pal_check('Wassamassaw - a town in South Dakota'))



