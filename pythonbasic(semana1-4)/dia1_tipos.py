proyecto = "mision ia"
semanas_totales = 78
porcentaje_actual = 0.01
mision_activa = True
dia = {
    1: "lunes",
    2: "martes",
    3: "miércoles",
    4: "jueves",
    5: "viernes",
    6: "sábado",
    7: "domingo"
}

print(proyecto.upper()[0:6])
print(f"inicio: {proyecto} - duración: {semanas_totales} semanas")

semana = 1

while semana <= semanas_totales and mision_activa:
    for i in range(1, 8):
        print(f"El día es: {dia[i]} y la semana es: {semana}")
    semana += 1

print("¡Misión completada!")
