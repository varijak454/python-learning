
# Importig libraries 
import random
# to generate random number list 
numbers = random.sample(range(1, 50), 7) 
# printing result 
print ("Random number list is : " +  str(numbers)) 
# Sorting on Ascending order
numbers.sort()
print("Sording Ascending order:", numbers)
# Sorting on descending order
numbers.sort(reverse=True)
print("Sording Descending Order:", numbers)