'''
1 - Cree un programa llamado reloj.py que simule un reloj con horas, minutos y segundos que
comience a contar desde 00:00:00 y termine en 23:59:59.
'''
import time

# Muestra hora

for hora in range(24):
    for minuto in range(60):
        for segundos in range(60):
            print(f"{hora}:{minuto}:{segundos}")

# Contador

for hora in range(24):
    for minuto in range(60):
        for segundos in range(60):
            print(f"{hora:02}:{minuto:02}:{segundos:02}", end="\r")
            time.sleep(1)