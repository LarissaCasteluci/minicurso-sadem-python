'''
	Calculo da Integral de Riemann de uma função exponencial de 0 a 1
'''

import math

real = math.exp(1) - math.exp(0)
print("Valor real:", real)

step = 1/100
total = 0
y = 0

while True :
    if y >= 1:
        break
    total += math.exp(y)*step
    y += step
    
print("Valor calculado:", total)

print("Erro:", real - total)