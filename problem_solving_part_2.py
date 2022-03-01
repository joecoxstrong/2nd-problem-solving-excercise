# Happy numbers
# When searching for happy numbers the code will run until it hits a result of either 1 or 4. 
# 1 means it is a happy number, 4 means it is not a happy number. All other results will keep looping


from math import sqrt


def sum_of_digits(n):
    res = 0
    rem = 0
    while n>0:
        rem = n%10
        res = res + rem * rem
        n = n//10
    return res
n = int(input("Enter a number and let's find out if it's Happy or Sad: "))
result = n
while result!=1 and result!=4:
    result = sum_of_digits(result)
if result == 1: 
    print(n, 'is a hapyy number')
else:
    print(n, 'is a sad number')



# Prime numbers

check_for_prime = int(input('Enter a number to check if it is a prime number: '))
def prime_test(num):
    if (num <= 1):
        return False
    for i in range(2, int(sqrt(num))+1):
        if (num % i == 0):
            return False    
    return True

if prime_test(check_for_prime):
    print(check_for_prime, 'is a prime number')
else:
    print(check_for_prime, 'is not a prime number')



# Fibonacci
n=int(input('Input n: '))
n = (n-1) + (n)
print(n)
#Finonacci sequence starting at 0
num_of_terms = int(input("Enter the number of terms you want to run: "))
num_1 = 0
num_2 = 1
count = 0

if num_of_terms <= 0:
    print('Terms must be a positive intiger.')
elif num_of_terms == 1: 
    print(num_1)
else: 
    while count < num_of_terms:
        print(num_1)
        num_to_nth_terms = num_1 + num_2
        num_1 = num_2
        num_2=num_to_nth_terms
        count+=1
