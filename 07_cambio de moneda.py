#Acabamos de llegar de un divertido viaje a Sudamérica, concretamente a Colombia, Perú y Brasil. Nos queda algo de efectivo:

#🇨🇴 pesos colombianos
#🇵🇪 Soles peruanos
#🇧🇷 Reales brasileños
#Crea un programa currency.py que pregunte al usuario el monto que tiene en pesos, soles y reales y calcule el total en USD.

co=float(input('Cuanto te sobro en co? :'))
usd=float(input ('ingrese el valor del dolar co:'))
pe=float(input('Cuanto te sobro en pe? :'))
usd=float(input ('ingrese el valor del dolar pe:'))
br=float(input('Cuanto te sobro en br? :'))
usd=float(input ('ingrese el valor del dolar br:'))

a=co*usd
b=pe*usd
c=br*usd

Total=a+b+c

print(Total)
