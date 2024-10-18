#se solicita los datos por consola al usuario
materia = input ("por favor ingrese el nombre de la materia:  ")
calificacion1 =float(input("por favor ingrese la calificacion 1: "))
while calificacion1 < 0 or calificacion1 >5:
    print("Error La calificación debe ser de 0 y 5")
    calificacion1 = float(input("Ingrese la calificación 1 en un rango de 0 a 5: "))

calificacion2 = float(input("por favor ingrese la calificacion 2: "))
while calificacion1 < 0 or calificacion2 > 5:
    print("Error La calificación debe ser de 0 y 5")
    calificacion2 = float(input("Ingrese la calificación 2 en un rango de 0 a 5: "))
calificacion3 = float(input("por favor ingrese la calificacion 3: "))
while calificacion1 < 0 or calificacion3 > 5:
    print("Error La calificación debe ser de 0 y 5")
    calificacion3 = float(input("Ingrese la calificación 3 en un rango de 0 a 5: "))

#calulcar las calificacion
definitiva =  (calificacion1*0.30)+(calificacion2*0.20)+(calificacion3*0.50)

if definitiva >=3.0:
    print("La Materia de " + materia + " usted la aprobo con :"+ str(round(definitiva, 1)))
else:
    print("La materia de "+ materia +" usted la reprobo con: " +str(round(definitiva, 1)))


















