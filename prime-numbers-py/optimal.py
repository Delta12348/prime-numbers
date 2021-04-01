from bitarray import bitarray
#4294967296
prime_numbers = bitarray(100)

prime_numbers.setall(True)
array_length = len(prime_numbers)

factor = 3
while factor < array_length:
    print(factor)
    index = factor
    while index < array_length:
        index += factor
        if index <= array_length:
            if prime_numbers[index - 2] == True:
                prime_numbers[index - 2] = False 
    factor += 2
    if prime_numbers[factor - 2] == False:
        factor += 2

numbers = [2]
index = 3
while index < array_length:
    if prime_numbers[index - 2] == True:
        number = index
        numbers.append(number)
    index += 2
print(numbers)
list_length = len(numbers)
print(list_length)
