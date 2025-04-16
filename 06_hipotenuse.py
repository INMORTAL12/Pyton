#Si te quedaste dormido en la clase de geometría, el teorema de Pitágoras es la relación entre los tres lados de un triángulo rectángulo. Recibe su nombre del filósofo griego Pitágoras, nacido alrededor del año 570 a. C.

#La ecuación de Pitágoras se ve así:



 

# Elaes la longitud de un lado corto.
#Elbes la longitud de otro lado corto.
#Eldoes la longitud de la hipotenusa.
#La hipotenusa es el lado más largo del triángulo rectángulo.

#Cree un programa hypotenuse.py que le pida al usuario dos números, ay b, y luego calcule la hipotenusa c.


a = int(input('ingrese numero a:'))
b = int(input('ingrese numero b:'))
c = int(input('ingrese numero c:'))

g=-b - (b**2- 4 * a * c)**0.5
f=-b + (b**2- 4 * a * c)**0.5

x1= g/2*a
x2=f/2*a


print(x1)
print(x2)
