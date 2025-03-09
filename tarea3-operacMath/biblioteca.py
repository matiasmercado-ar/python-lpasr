"""
2 - Luego cree otro programa llamado biblioteca.py. En este caso se plantea lo siguiente. Tiene dos
esferas, la esfera 1 presenta un radio de 5 cm y la esfera 2 presenta un radio de 12.5 cm. ¿Cuál es la
diferencia de volumen entre las dos esferas?
"""
import math

radio1 = 5  
radio2 = 12.5 

# Calcular los volúmenes usando la fórmula: V = (4/3) * π * r³
volumen1 = (4/3) * math.pi * (radio1 ** 3)
volumen2 = (4/3) * math.pi * (radio2 ** 3)

dif_volumen = volumen2 - volumen1
dif_volumen = round(dif_volumen,2)

print(f"La diferencia de volumen es: {dif_volumen:} cm³")
