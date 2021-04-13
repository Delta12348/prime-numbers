import numpy as np
from numba import njit, vectorize

digits = int(input("Number to calculate: "))
prime_numbers = np.ones(digits)
array_length = len(prime_numbers)
factor = 2

@njit 
def calculate_prime_numbers(factor, length, array):
  while factor < array_length:
    print(factor)
    index = factor
    while index < array_length:
      index += factor
      if index <= length:
        if array[index - 1] == True:
          array[index - 1] = False
    factor += 1
    if array[factor - 1] == False:
      while array[factor - 1] == False:
        factor += 1
        if factor > length:
          break
  return array

primes = calculate_prime_numbers(factor=factor, length=array_length, array=prime_numbers)
