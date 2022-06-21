import sys

if int((sys.argv[1])) < 10 and int((sys.argv[1])) > 0 and int((sys.argv[2])) < 10 and int((sys.argv[2])) > 0):
    if (sys.argv[1]) and (sys.argv[2]) > 7:
        print("Promocionado")
    elif (sys.argv[2]) and (sys.argv[1]) >= 4:
        print("Aprobado, debe rendir final")
else:
    print("Error")

#Correcto:
import sys


''' genere un script que reciba por parametro 2 notas, y
si ambas son > 7 imprima aprobado, si no imprima reprobado '''

if len(sys.argv) == 3:
    nota1 = float(sys.argv[1])
    nota2 = float(sys.argv[2])

    if nota1>=7 and nota2>=7:
        print("Promocionado")
    elif nota1>=4 and nota2>=4:
        print("Aprobado")
    elif (nota1<4 or nota2<4) and (not (nota1<4 and  nota2<4)):
        if nota1<4:
            print("recupera el primer parcial")
        else:
            print("recupera el segundo parcial")
    else:
        print("desaprobo los 2 parciales")
else:
    print("Error, debe ingresar 2 notas")


#Nuestro corregdo
if int((sys.argv[1])) < 10 and int((sys.argv[1])) > 0 and int((sys.argv[2])) < 10 and int((sys.argv[2])) > 0:
    if int((sys.argv[1])) and int((sys.argv[2])) > 7:
        print("Promocionado")
    elif int((sys.argv[2])) and int((sys.argv[1])) >= 4:
        print("Aprobado, debe rendir final")
else:
    print("Error")
