# for example lets take an example of number 10
# Recursive case - the flow
# first we've to think that how can we separate this number in digits 1 and 0
# to do this we've to divide this number by 10, so we get quotient 1 and remainder 0
# 54 = 54/10 = 5 and remainder 4
# 112 = 112/10 = 11 and remainder 2
#         11 = 1 and remainder 1
# Base case

def sum_of_digits(n):
    assert n >= 0 and int(n) == n, "The number must be positive integer only."
    if n == 0:
        return 0
    else:
        return n%10 + sum_of_digits(n//10)
print(sum_of_digits(0))