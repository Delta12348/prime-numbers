from bitarray import bitarray
#4294967296
prime_numbers = bitarray(100)

prime_numbers.setall(True)
array_length = len(prime_numbers)

factor = 2
while factor < array_length:
    print(factor)
    index = factor
    while index < array_length:
        index += factor
        if index <= array_length:
            if prime_numbers[index - 1] == True:
                prime_numbers[index - 1] = False 
    factor += 1
    if prime_numbers[factor - 1] == False:
        factor += 1

numbers = []
index = 2
while index < array_length:
    if prime_numbers[index - 1] == True:
        number = index
        numbers.append(number)
    index += 1
print(numbers)
list_length = len(numbers)
print(list_length)
