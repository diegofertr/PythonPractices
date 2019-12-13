# -*- coding: utf-8 -*-

def palindrome1(word):
  if word == word[::-1]:
    return True

  return False



def palindrome2(word):
  reversed_word = word[::-1]

  if reversed_word == word:
    return True

  return False

def palindrome(word):
  reversed_letters = []

  for letter in word:
    reversed_letters.insert(0, letter)

  reversed_word = ''.join(reversed_letters)

  if reversed_word == word:
    return True

  return False


if __name__ == '__main__':
  word = str(input('Escribe una palabra: '))

  if palindrome2(word) is True:
    print('{} sí es un palíndromo.'.format(word))
  else:
    print('{} no es un palíndromo.'.format(word))
