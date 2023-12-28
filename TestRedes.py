
from Tablasderedes import *

# B/24 200
# C/25 100
# A/26 37
# E/30 2

# A/26 37
# B/24 200
# C/25 100
# E/30 2

topologia_completa = IPNetwork('192.168.0.0/16')
# # -------------------------------12 líneas---------------------------------------------Inicia sección probada
# departamento_B = filetear(topologia_completa, prefijo=24, primero=True)
# departamento_C = filetear(departamento_B, prefijo=25)
# departamento_A = filetear(departamento_C, prefijo=26)

# e1, e2, e3 = filetear(topologia_completa, n_enlaces=3)

# topologia_completa = Segmento(topologia_completa, 'Topología')
# departamento_B = Segmento(departamento_B, 'Departamento B')
# departamento_C = Segmento(departamento_C, 'Departamento C')
# departamento_A = Segmento(departamento_A, 'Departamento A')
# e1 = Segmento(e1, 'Enlace 1')
# e2 = Segmento(e2, 'Enlace 2')
# e3 = Segmento(e3, 'Enlace 3')
# # ----------------------------------------------------------------------------Termina sección probada
# --------------------------9 líneas-------------------------- Comienza sección más elegante de escribir
departamento_B = Segmento(filetear(topologia_completa, prefijo=24, primero=True), 'Departamento B')
departamento_C = Segmento(filetear(departamento_B, prefijo=25), 'Departamento C')
departamento_A = Segmento(filetear(departamento_C, prefijo=26), 'Departamento A')
e1, e2, e3 = filetear(topologia_completa, n_enlaces=3)
e1 = Segmento(e1, 'Enlace 1')
e2 = Segmento(e2, 'Enlace 2')
e3 = Segmento(e3, 'Enlace 3')
topologia_completa = Segmento(topologia_completa, 'Topología')
# ---------------------------------------------------- Termina sección más elegante de escribir

tabla_entera = [topologia_completa, departamento_A, departamento_B, departamento_C, e1, e2, e3]

for segmento in tabla_entera:
    print(segmento)