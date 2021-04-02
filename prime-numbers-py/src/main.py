from bitarray import bitarray
#4294967296, this is the number the algorithm is looking forward to achieve
prime_numbers = bitarray(100000000) # The number is just for testing purposes

prime_numbers.setall(True) #The program starts by making all the bit in the Array true, making it think all the numbers are prime before test
array_length = len(prime_numbers) #Takes the length of the array

factor = 2 #Starts by testing two as a valid factor for a prime number
while factor < array_length: #While the factor to test is less than the length of the array
    print(factor) #Used to know what is the current factor being tested
    index = factor # To make the program function as a multiple fashioned way but arithmetically efficient. The index starts as the factor
    while index < array_length: #While the index is less than the length of the array
        index += factor # Adds up index plus the factor. For example 2 + 2 = 4, 4 + 2 = 6. This is used to know the multiples
        if index <= array_length: #To avoid errors before turning a bit into false, the program tests if index is not out of range with the index
            if prime_numbers[index - 1] == True: #If the index is thought to be a prime number 
                prime_numbers[index - 1] = False #That number is now not a prime number
    factor += 1 #When finished testing the first factor increase the test factor by one
    if prime_numbers[factor -1] == False: #Test if the factor added is considered a possible prime
        while prime_numbers[factor-1] == False: #If it is not valid, test until you find a valid prime adding by two
            factor += 1
            if factor > array_length: #To avoid range error, break the loop if the factor is more than the length of the array
                break

numbers = [] #When finishing testing all the factors create an empty list with no numbers in it
index = 2 #Start by testing the first factor
while index < array_length: #While the index is less that the length of the array
    if prime_numbers[index - 1] == True: #If the bit in that index position is recognized as True
        number = index #Create a copy of the index called number
        numbers.append(number) #Append that prime number into the list 
    index += 1 #Check the bit of the next position<
print(numbers)#After finishing to test all numbers, show the list of the primes
list_length = len(numbers) #This is for testing purposes
print(list_length) #Print to show that the number of prime numbers found are correct
