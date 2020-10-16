import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la multiplicacion de 3 numeros
2*4*3 = 24
"""


# start-->
def multiplicar():
    result = 2*4*3
    return result


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros divisibles entre 3 y 5 del 1000 al 2000
"""


# start-->
def sumaDivTresYCincoPlus():
    numero = 1000
    result= 0
    while numero < 2000:
        if (numero%3 ==0) and (numero%5==0):
            result = result + numero
            numero+=1
        else:
            numero+1

    
    return result




"""
***************************************************************
@@ ejercicio 3 @@
encontrar el area y el volumen de un ortoedro
longitud = 10 m
latitud = 6 m
altura = 5 m
area: A = 2(longitud · latitud + longitud · altura + latitud · altura)
volumen: V = longitud · latitud · altura
"""


# start-->
def definicionOrtoedro():
    area = obtenerArea()
    volumen = obtenerVolumen
    result = {
        "area": area,
        "volumen":volumen
    }
    return result


def obtenerArea():
    result =2*(10* 6 + 10 * 5 + 6 * 5)
    return result


def obtenerVolumen():
    result = 10 * 6 * 5
    return result


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase
"""


# start-->
class Ortoedro:
    def definicionOrtoedro(self):
        area = obtenerArea()
        volumen = obtenerVolumen
        result = {
        "area": area,
        "volumen":volumen
        }
        return result
    def obtenerArea(self): 
        result =2*(10* 6 + 10 * 5 + 6 * 5)
        return result

    def obtenerVolumen(self): 
        result = 10 * 6 * 5
        return result   


"""
***************************************************************
@@ ejercicio 5 @@
VentaComputadoras
Computadora
    procesador
    ram
    tarjeta_grafica
    ssd
    costo
    conDescuento
    descuento
    conPlazo
    cuota
"""


class VentaComputadoras:
    def orden(self):
        pass

    def totalProcesadorIntel(self):
        return 0

    def totalRam16ConDescuento(self):
        return 0


class Computadora:
    pass


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return ""