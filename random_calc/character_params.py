from random import randrange
proxsum = 0
iterations = 100000
j = 0
while j < iterations:
    sigma = 0
    throws = []    
    for i in range(5):                      # Бросается 5 кубов
        throws.append(randrange(1,5))       # 1к4
    minimal_throw = min(throws)             # Выделяется минимальынй бросок
    sigma = sum(throws)                     # Суммируются броски
    proxsum += sigma - minimal_throw        # Из суммы вычитается минимальный бросок
    j += 1
print(proxsum/iterations)

# средний стат, выпадаемый с кубов = 11,22