#CALCULADORA


def suma(num1, num2):
    return num1 + num2;

def resta (num1, num2):
    return num1 - num2;

def multiplicacion (num1,num2):
    return num1 * num2;

def division(num1, num2):
    if num2 == 0:
        raise ValueError("No se puede dividir entre 0.")
    return (num1 / num2)

def divisionEntera(num1, num2):
    if num2 == 0:
        raise ValueError("No se puede dividir entre 0.")
    return (num1 // num2)

def potencia (num1, num2):
    return (num1 ** num2)

print ("Operaciones:")
print ("1. Suma")
print ("2. Resta")
print ("3. Multiplicacion")
print ("4. Division")
print ("5. Division Entera")
print ("6. Potencia")

op=(input("Selecciona la operación que deseas hacer (1/2/3/4/5/6):"))


try: 
    num1=int(input('¿cuál es el primer número?: '))
    num2=int(input('¿cuál es el segundo número?: '))

    if op =='1':
        print ('el resultado de la suma es: ', suma(num1, num2))
    elif op == '2':
        print ('el resultado de la resta es: ', resta(num1, num2))
    elif op == '3':
        print('el resultado de la multiplciación es: ', multiplicacion(num1, num2))
    elif op == '4' :
        print('El resultado de la división es: ', division(num1, num2))
    elif op == '5' :
        print('El resultado de la división entera es: ', divisionEntera(num1, num2))
    elif op == '6' :
        print('El resultado de la potencia es: ', potencia(num1, num2))
    else:
        print('opcion no válida, intenta de nuevo.')
        
except ValueError as ve:
    print("Error:", ve)
except Exception as e:
    print("Ha ocurrido un error:", e)