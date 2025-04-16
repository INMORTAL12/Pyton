#calculadora basica

print("Calculadora simple")
print("Operaciones disponibles: +, -, *, /, %")

# Solicitud del usuario
num1 = float(input("Ingresa el primer número: "))
operador = input("Puedes ingresar las operaciones  (+, -, *, /, %): ")
num2 = float(input("Ingresa el segundo número: "))

# calculadora
if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Error"
elif operador == "%":
    resultado = num1 % num2
else:
    resultado = "Operador no válido"

print("Resultado es :", resultado)

# sin while True
# con while True

print("Calculadora en Python")
print("Operaciones disponibles: +, -, *, /, %")
print("Escribe 'salir' como operador para terminar.\n")

while True:
    try:
        num1 = float(input("Ingresa el primer número: "))
        operador = input("Ingresa el operador (+, -, *, /, %, salir): ")
        
        if operador.lower() == "salir":
            print("Saliendo de la calculadora. ¡Hasta pronto!")
            break

        num2 = float(input("Ingresa el segundo número: "))

        if operador == "+":
            resultado = num1 + num2
        elif operador == "-":
            resultado = num1 - num2
        elif operador == "*":
            resultado = num1 * num2
        elif operador == "/":
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = "Error: División por cero"
        elif operador == "%":
            resultado = num1 % num2
        else:
            resultado = "Operador no válido"

        print("Resultado:", resultado)
        print("-" * 30)

    except ValueError:
        print("❌ Entrada no válida. Por favor, escribe solo números.")
        print("-" * 30)