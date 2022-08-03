# step1 - Recursive case
# 1. divide the number by 2
# 2. get the integer quotient for the next iteration
# 3. get the remainder for the binary digit
# 4. Repeat the steps until the quotient is equal to 0.
# 13 to binary
# Division by   quotient    Remainder
# 13/2              6          1
# 6/2               3          0
# 3/2               1          1
# 1/2               0          1
# result = 13 in binary is 1101

def decTobin(n):
    assert int(n) == n, "Number must be integer only."
    if n == 0:
        return 0
    else:
        return n % 2 + decTobin(int(n/2)) * 10
print(decTobin(1.3))