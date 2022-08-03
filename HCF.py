# A HCF is a largest positive integer that divide the number without remainder.
# 8 = 2*2*2
# 12 = 2*2*3
# so HCF = 2*2 = 4
# Euclidean algorithm = is a way of finding the hcf of numbers.
# recursive case - the flow = hcf(a,0) = a
#                             hcf(a,b) = hcf(b,a%b)
# Base case - the stopping case
# b = 0
# constraint case -
# 1. hcf must be positive integer only 2. convert negative number to positive

def hcf(a, b):
    assert int(a) == a and int(b)== b, "Numbers must be positve integer only."
    if a < 0:
        a *= -1
    if b < 0:
        b *= -1
    if b == 0:
        return a
    else:
        return hcf(b, a%b)
print(hcf())
