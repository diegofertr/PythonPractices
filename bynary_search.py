# -*- coding: utf-8 -*-

def bynary_search(numbers, number_to_find, low, high):
  if low > high:
    return False

  mid = int((low + high) / 2)

  if numbers[mid] == number_to_find:
    return True

  elif numbers[mid] > number_to_find:
    return bynary_search(numbers, number_to_find, low, mid - 1)
  else:
    return bynary_search(numbers, number_to_find, mid + 1, high)


if __name__ == '__main__':
  numbers = [1, 3, 4, 88, 6, 9, 10, 34, 2, 45, 28, 49, 51, 27]
  numbers.sort()

  number_to_find = int(input('Ingresa un número: '))

  result = bynary_search(numbers, number_to_find, 0, len(numbers) - 1)

  if result is True:
    print('El número SI está en la lista')
  else:
    print('El número NO está en la lista')