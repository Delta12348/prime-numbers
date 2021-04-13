import numpy as np
from numba import njit, vectorize

digits = int(input("Number to calculate: "))
threads = int(input("Number of threads in system: "))
prime_numbers = np.ones(digits)
array_length = len(prime_numbers)
factor = 3

@njit 
def calculate_prime_numbers(factor, length, array):
  while factor < array_length:
    print(factor)
    index = factor
    while index < array_length:
      index += factor
      if index <= length:
        if array[index - 2] == True:
          array[index - 2] = False
    factor += 2
    if array[factor - 2] == False:
      while array[factor - 2] == False:
        factor += 2
        if factor > length:
          break
  return array

primes = calculate_prime_numbers(factor=factor, length=array_length, array=prime_numbers)