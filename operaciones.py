#CALCULADORA


def suma(num1, num2):
    return num1 + num2;

def resta (num1, num2):
    return num1 - num2;

def multiplicacion (num1,num2):
    return num1 * num2;

print ("Operaciones:")
print ("1. Suma")
print ("2. Resta")
print ("3. Multiplicacion")

op=(input("Selecciona la operación que deseas hacer (1/2/3):"))


num1=int(input('¿cuál es el primer número?'))
num2=int(input('¿cuál es el primer número?'))

if op =='1':
    print ('el resultado de la suma es: ', suma(num1, num2))
elif op == '2':
    print ('el resultado de la resta es: ', resta(num1, num2))
elif op == '3':
    print('el resultado de la multiplciación es: ', multiplicacion(num1, num2))
else:
    print('opcion no válida, intenta de nuevo.')