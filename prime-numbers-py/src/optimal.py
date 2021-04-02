from bitarray import bitarray 
#4294967296, this is the number to beat 
prime_numbers = bitarray(100000000) #Creates an array of bits of the specified length

prime_numbers.setall(True) #Sets all the bits in the array true
array_length = len(prime_numbers) #Takes the length of that array, naturally the specified number 

factor = 3 #This may be cheating but is far more efficient than the normal solution, since we already know that all multiples of 2 are non-prime we can just begin testing with three and forgeting all multiples of 2 
while factor < array_length: #While the factor to test is less than the length of the array 
    print(factor) #This is used to know what is the factor being currently tested 
    index = factor #To make the program function as a multiple fashioned way but arithmetically efficient, we make the index be of same value as the factor
    while index < array_length: #While the index is less than the array length
        index += factor #Add the index wih the factor e.g. 3 + 3 = 6, 6 + 3 = 9
        if index <= array_length: #This is safe coding to avoid the addition to be aout of index
            if prime_numbers[index - 2] == True: # If the bit in which the index is currently at is considered as a prime number
                prime_numbers[index - 2] = False #Make that bit a non-prime number 
    factor += 2 #Since we already know that no multiple of two can be a prime number with simply skip to the next number e.g. 3 + 2 = 5 (Next factor to test)
    if prime_numbers[factor -2] == False: #Test if the new factor is a possible prime
        while prime_numbers[factor-2] == False:  #If not, keep adding until you find a new prime
            factor += 2 
            if factor > array_length: #To avoid range error, break the loop if the factor is bigger than the length of the array
                break

numbers = [2] #We already know that two is a prime number so we add it to the list 
index = 3 #For the same reason we start testing the bits from number three
while index < array_length: #While the index is less than the array length
    if prime_numbers[index - 2] == True: #If the current index position is considered as a prime number 
        number = index #Make a copy of the index
        numbers.append(number) #Index that copy as the prime number 
    index += 2 # Skips to test the next uneven number
print(numbers) # Prints all the prime numbers
list_length = len(numbers) #Print the number of prime numbers for test purposes
print(list_length)
