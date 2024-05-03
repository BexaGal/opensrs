from random import randrange

cubetype = int(input("Enter cube type: "))
cubenum = int(input("Number of corresponding cubes: "))
additionaldamage = int(input("Additional constant damage: "))
icount = int(input("Nuber of desireble iterations: "))

damsum = 0
for iteration in range(icount):
    for i in range(cubenum):
        damsum = damsum + randrange(1, (cubetype + 1)) + additionaldamage

print("Avg damage is: " + str((damsum / icount)) )