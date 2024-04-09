# "0401608260#Magaly#Chulde#9.5#6.5#7.5",
def buscarEstudiante(cedula,listaEstudiante):
    for est in listaEstudiante:
        partesEstudiante=est.split("#")
        if partesEstudiante[0]==cedula:
            return est
    return None
def calcularTotal(n1, n2, n3, faltas):
    if faltas == 0:
        n4 = 10
    elif faltas < 4:
        n4 = 9
    elif faltas < 6:
        n4 = 8
    else:
        n4 = 7

    total = (n1 + n2 + n3 + n4) / 4
    return round(total, 2)
def calcularPromedioCurso(listaEstudiantes):
    totalSuma = 0
    cantidadEstudiantes = len(listaEstudiantes)

    for est in listaEstudiantes:
        partesEstudiante = est.split("#")
        total = float(partesEstudiante[-1])  # Última posición es la nota total
        totalSuma += total

    if cantidadEstudiantes > 0:
        promedioCurso = totalSuma / cantidadEstudiantes
        return round(promedioCurso, 4)
    else:
        return 0
