# -*- coding: utf-8 -*-
import random

def run(limite):
  number_found = False
  random_number = int(random.randint(0, limite))

  while not number_found:
    number = int(input('Intenta adivinar el número: '))
    
    if number == random_number:
      print('Felicidades. Encontraste el número')
      number_found = True
    elif number > random_number:
      print('El número es más pequeño')
    else:
      print('El número es más grande')

if __name__ == '__main__':
  limite = int(input('Introduzca el número límite del juego > '))
  run(limite)
