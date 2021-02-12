def determine_prime(pn):#taking pn as parameter, defining function.
    if pn <= 1:#if pn is 0 or 1 and not pn is not prime number.
        return False
    for i in range(2, pn):
        if pn % i == 0:
            return False
    else :
        return True
for k in range(32):#generates k from 1 to 32.
    pn = 3**k - 2**k
    if determine_prime(pn):#calling the "determine_prime" function.
        try:
            print(pn)
        except AssertionError as error:
            print(error)






