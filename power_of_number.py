# Recursive case - the flow
# 2 ** 2 = 2*2 =4
# 3**3 = 3*3 = 9
# 4**4 = 4*4*4*4 = 256
# n * power_of_number(n,p-1)
# Base case - n=0, n=1
# constraint case - (-1,2),(2,-2),(1.2,4),(4,2.5)

def power_of_number(n, p):
    assert p >= 0 and int(p) == p, "The power must be integer and greater than to 0"
    if p == 0: # if p in [0,1]: return n
        return 1
    else:
        return n * power_of_number(n, p-1)

print(power_of_number(4,2.5))