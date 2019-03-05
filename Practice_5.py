#!/bin/python

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
if (N%2!=0):
    print("Weird")

else:
    if (N>1 and N<6):
        if(N%2==0):
            print("Not Weird")
    elif (N>5 and N<21):
        print("Weird")
    else:
        print("Not Weird")
#_______________________________________________________________


def is_leap(year):
    leap = False
    if (year%100==0):
        if(year%400==0):
          leap=True
    elif (year%4==0):
        leap=True
    return leap
year = int(input())

#____________________________________________________

from __future__ import print_function

if __name__ == '__main__':
    n = int(input())
    string=""
    for i in range(1,n+1):
        string+=str(i)
    print(string)


#____________________________________________________

number_of_english=int(input())
input1=input()
number_of_french=int(input())
input2=input()
list_of_english=input1.split(" ")
list_of_french=input2.split(" ")
count=0
for element in list_of_english:
    if element in list_of_french:
        count+=1
print(count)

#___________________________________________________

# Enter your code here. Read input from STDIN. Print output to STDOUT
number_of_english=int(input())
input1=input()
number_of_french=int(input())
input2=input()
list_of_english=input1.split(" ")
list_of_french=input2.split(" ")
count=0
for element in list_of_english:
    if element not in list_of_french:
        count+=1
print(count)
#____________________________________________________
# Enter your code here. Read input from STDIN. Print output to STDOUT
number_of_english=int(input())
input1=input()
number_of_french=int(input())
input2=input()
list_of_english=input1.split(" ")
list_of_french=input2.split(" ")
count=0
for element in list_of_english:
    if element in list_of_french:
        count+=2
count=len(list_of_french)+len(list_of_english)-count
print(count)
#____________________________________________________


# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
A = set(map(int, input().split()))
for i in range(int(input())):
    s, b = input().split()
    if s == 'intersection_update':
        A &= set(map(int, input().split()))
    elif s == 'update':
        A |= set(map(int, input().split()))
    elif s == 'symmetric_difference_update':
        A ^= set(map(int, input().split()))
    else:
        A -= set(map(int, input().split()))
print (sum(A))

#____________________________________________________

# Enter your code here. Read input from STDIN. Print output to STDOUT
K = int(input())
roomList = map(int,input().split())
roomSet = set(roomList)
sumRoomSet = sum(roomSet)
sumRoomList = sum(roomList)
temp = sumRoomSet * K - sumRoomList
answer = temp / (K - 1)
print (answer)

#_________________________________________________________
# Enter your code here. Read input from STDIN. Print output to STDOUT
test_cases = int(input())
for i in range(0, test_cases):
    counter = 0
    set_a_number = input()
    set_a = input().split()
    set_b_number = input()
    set_b = input().split()
    for element in set_a:
        if element in set_b:
            counter += 1

    if (counter == len(set_a)):
        print(True)
    else:
        print(False)

#_____________________________________________________

# Python program to count positive and negative numbers in a List 

# list of numbers 
list1 = [10, -21, 4, -45, 66, -93, 1]

pos_count, neg_count = 0, 0

# iterating each number in list 
for num in list1:

    # checking condition 
    if num >= 0:
        pos_count += 1

    else:
        neg_count += 1

print("Positive numbers in the list: ", pos_count)
print("Negative numbers in the list: ", neg_count) 
#____________________________________________________

# Function to Check if frequency of all characters
# can become same by one removal
from collections import Counter


def allSame(input):
    # calculate frequency of each character
    # and convert string into dictionary
    dict = Counter(input)

    # now get list of all values and push it
    # in set
    same = set(dict.values())

    # now check if frequency of all characters
    # can become same
    if (len(same) == 1):
        print
        'Yes'
    elif (len(same) == 2):
        if (list(same)[0] == 1):
            print
            'Yes'
        else:
            print
            'No'


# Driver program
if __name__ == "__main__":
    input = 'xxxxyyzz'
    allSame(input)

#____________________________________________________


# Python3 code to find largest prime
# factor of number
import math


# A function to find largest prime factor
def maxPrimeFactors(n):
    # Initialize the maximum prime factor
    # variable with the lowest one
    maxPrime = -1

    # Print the number of 2s that divide n
    while n % 2 == 0:
        maxPrime = 2
        n >>= 1  # equivalent to n /= 2

    # n must be odd at this point,
    # thus skip the even numbers and
    # iterate only for odd integers
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            maxPrime = i
            n = n / i

            # This condition is to handle the
    # case when n is a prime number
    # greater than 2
    if n > 2:
        maxPrime = n

    return int(maxPrime)


# Driver code to test above function
n = 15
print(maxPrimeFactors(n))

n = 25698751364526
print(maxPrimeFactors(n))
#____________________________________________________

# Python program to convert time
# from 12 hour to 24 hour format

# Function to convert the date format
def convert24(str1):
    # Checking if last two elements of time
    # is AM and first two elements are 12
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]

        # remove the AM
    elif str1[-2:] == "AM":
        return str1[:-2]

        # Checking if last two elements of time
    # is PM and first two elements are 12
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]

    else:

        # add 12 to hours and remove PM
        return str(int(str1[:2]) + 12) + str1[2:8]

    # Driver Code


print(convert24("08:05:45 PM"))
#____________________________________________________


