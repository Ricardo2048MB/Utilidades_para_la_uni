def agregar_tiempo(tiempo_inicial, tiempo_agregado, dia_inicial=None):
    # t = [día, días transcurridos, am/pm, hh, mm]
    # ________________Empieza la zona de inicialización_____________________________________
    dia_de_la_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    # Primero voy a obtener la información pertinente.
    # Asigno el formato y los tiempos por separado.
    z = [0, 0, 0, 0, 0] # El usuario nunca debe poder establecer los días transcurridos con el segundo elemento del primer parámetro.
    # Deberá hacerlo la operación, cuando ya todo se sume con la información del segundo parámetro.
    if dia_inicial != None:
        for dia in dia_de_la_semana:
            if dia == dia_inicial.lower():
                z[0] = dia_de_la_semana.index(dia) # El usuario establece el día de la semana
                break

    # z[1] Nunca aparece siendo modificado porque el usuario no debe ser capapz de establecer los días transcurridos desde el primer parámetro, como se explica arriba.
    if tiempo_inicial.split()[1].lower() == "pm": # Modificación disjunta
        z[2] = 1
    z[3] = int(tiempo_inicial.split()[0].split(":")[0]) + int(tiempo_agregado.split(":")[0])
    z[4] = int(tiempo_inicial.split()[0].split(":")[1]) + int(tiempo_agregado.split(":")[1])
    # ________________Termina la zona de inicialización_____________________________________
    # ________________Empieza la zona de operaciones________________________________________

    # t = [día, días transcurridos, am/pm, hh, mm]
    z[4], acarreo = z[4] % 60, z[4] // 60 # Minutos
    z[3], acarreo = (z[3] + acarreo) % 12, (z[3] + acarreo) // 12 # Horas
    z[2], acarreo = (z[2] + acarreo) % 2, (z[2] + acarreo) // 2 # AM/PM
    z[1], z[0] = (z[1] + acarreo), (z[1] + z[0] + acarreo) % 7 # Días transcurridos, día (de la semana)
    # __________________________________________________________________________________________________Presentación de la información
    if dia_inicial != None:
        cadena_resultado = f"{dia_de_la_semana[z[0]]}"
        cadena_resultado += f" {z[3]}:{z[4]}"
    else:
        cadena_resultado = f"{z[3]}:{z[4]}"
    if z[2] == 0:
        cadena_resultado += " AM"
    elif z[2] == 1:
        cadena_resultado += " PM"

    if z[1] != 0:
        cadena_resultado += f" ({z[1]} día(s) después)"

    return cadena_resultado