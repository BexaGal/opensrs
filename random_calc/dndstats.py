from random import randrange
proxsum = 0
iterations = 1000000
j = 0
while j < iterations:
    sigma = 0
    throws = []    
    for i in range(4):
        throws.append(randrange(1,7))
    minimal_throw = min(throws)
    for i in range(len(throws)):
        sigma += throws[i]
    proxsum += sigma - minimal_throw
    j += 1
print(proxsum/iterations)