# segun el codigo indica si puede entrar al parque de atracciones si tienes los suficientes creditos y la suficiente altura
heigth = int(input('Cual es su altura:       '))
credits = int(input('Cuantos creditos tiene:   '))
if heigth >= 137 and credits > 10 :
 answer = 'disfruta el viaje'

elif heigth < 137 and credits >= 10 :
  answer = 'No eres lo suficientemente alto para viajar'

elif heigth >= 137 and credits <= 10:
  answer = 'No tiene suficientes créditos'

elif heigth < 137 and credits < 10:
  answer ='No cumple con los requisitos'

else:
  answer ='No cumple con los requisitos'

print('The ciclone indica:' +  answer)

