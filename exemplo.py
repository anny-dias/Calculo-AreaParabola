"""Calculando a area de uma parabola"""


def funcao(x):
    y = (-x**2) + (25 * x)
    return y

  
x = 0 
delta = 0.025
Area = 0

while x < 25:
    f = funcao(x)
    area = f * delta
    Area += area
    x += delta
print(Area)




    


"""Calculando pi"""

