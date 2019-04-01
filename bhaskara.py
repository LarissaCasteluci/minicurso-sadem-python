import math


def bhaskara(a,b,c):
    
    delta = b**2 - 4*a*c
    
    if delta < 0:
        print("O delta é negativo, não há solução")
    elif delta == 0:
        return -b/(2*a)
    else:
        r1 = (-b + math.sqrt(delta))/ (2*a)
        r2 = (-b - math.sqrt(delta))/ (2*a)
        return r1, r2
    
print(bhaskara(1, 12, -13))