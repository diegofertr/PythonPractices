# -*- coding: utf-8 -*-
import random

# por convencion en python las constantes se escriben con mayúsculas
IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
      |
      |
      |
      =========
  ''', '''
  +---+
  |   |
  O   |
      |
      |
      |
      |
      |
      |
      =========
  ''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
      |
      |
      |
      =========
  ''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
      |
      |
      |
      =========
  ''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
      |
      |
      |
      =========
  ''', '''
  +---+
  |   |
  O   |
 /|\  |
  |   |
      |
      |
      |
      |
      =========
  ''', '''
  +---+
  |   |
  O   |
 /|\  |
  |   |
 /    |
      |
      |
      |
      =========
  ''', '''
  +---+
  |   |
  O   |
 /|\  |
  |   |
 / \  |
      |
      |
      |
      =========
  '''
]

WORDS = [
  'javascript',
  'java',
  'python',
  'dart',
  'lavadora',
  'microondas',
  'gobierno',
  'teclado'
]

# Escoge aleatoriamente una palabra de la lista WORDS
def random_word():
  random_index = random.randint(0, len(WORDS) - 1)
  return WORDS[random_index]


def display_board(hidden_word, tries):
  print(IMAGES[tries])
  print('')
  print(hidden_word)
  print('--- * --- * --- * --- * --- * --- * --- * --- * --- * ---')


def run():
  word = random_word()
  hidden_word = ['-'] * len(word)
  tries = 0

  while True:
    display_board(hidden_word, tries)
    # current_letter = str(input('Escoge una letra: '))
    current_letter = str(raw_input('Escoge una letra: '))

    letter_indexes = []
    for index in range(len(word)):
      if word[index] == current_letter:
        letter_indexes.append(index)

    if len(letter_indexes) == 0:
      tries += 1

      if tries == len(IMAGES) -1:
        display_board(hidden_word, tries)
        print('')
        print('¡Perdiste! La palabra correcta era {}'.format(word))
        break

    else:
      for index in letter_indexes:
        hidden_word[index] = current_letter

      letter_indexes = []

    try:
      hidden_word.index('-')
    except ValueError:
      print('')
      print('¡Felicidades! Ganaste. La palabra es: {}'.format(word))
      break


if __name__ == "__main__":
  print('B I E N V E N I D O S       A       A H O R C A D O S')
  run()