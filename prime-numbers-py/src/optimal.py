import numpy as np
from numba import njit

digits = int(input("Number to calculate: "))
prime_numbers_array = np.ones(digits)
array_length = len(prime_numbers_array)
factor = 3

print(prime_numbers_array)

@njit(parallel=True)
def calculate_prime_numbers(factor, array):
  while factor < array_length:
    print(factor)
    index = factor
    while index < array_length:
      index += factor
      if index <= array_length:
        if array[index - 2] == True:
          array[index - 2] = False
    factor += 2
    if array[factor - 2] == False:
      while array[factor - 2] == False:
        factor += 2
        if factor > array_length:
          break
  return array

primes = calculate_prime_numbers(factor=factor, array= prime_numbers_array)