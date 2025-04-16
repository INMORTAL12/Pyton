

#Nueve respuetas que te indiquen tu respectiva pregunta

import random

Pregunta = input ('Pregunta:    ')
random_ball = random.randint(1, 9)

if random_ball == 1:
 respuesta ='si,definitivamente'

elif random_ball == 2:
 respuesta ='Definitivamente es así'

elif random_ball == 3:
 respuesta='Sin duda'

elif random_ball == 4:
 respuesta='Respuesta confusa, inténtalo de nuevo'

elif random_ball == 5:
 respuesta='Vuelve a preguntar más tarde.'

elif random_ball == 6:
 respuesta='Mejor no te lo digo ahora.'

elif random_ball == 7:
 respuesta='Mis fuentes dicen que no.'

elif random_ball == 8:
 respuesta='Las perspectivas no son muy buenas.'

elif random_ball == 9:
 respuesta='Muy dudoso.'

else:
  respuesta = 'Error'

print('bola 8 magico:' + respuesta)



