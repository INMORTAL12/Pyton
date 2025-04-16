#En química, el pH es una escala utilizada para especificar la acidez o basicidad de un líquido. 🧪

#Cree un programa ph_levels.py que verifique si un nivel de pH es básico, ácido o neutro.

#Primero, crea una phvariable y pídele al usuario un valor entre 0 y 14.

#Escribe una ifafirmación que elifdiga else:

#Si phes mayor que 7, salida "Básico".
#Si phes menor que 7, salida "Ácido".
#De lo contrario, salida "Neutral".

ph = int(input("ingrese el valor de ph de 0-14 : "))

if ph > 7 :
  print("basico")
elif ph < 7 :
  print("acido")
else:
  print("neutral")  
