"""
https://www.hackerrank.com/challenges/write-a-function/problem-1
"""

def is_leap(year):
    leap = False
    if (year%100==0):
        if(year%400==0):
          leap=True
    elif (year%4==0):
        leap=True
    return leap
year = int(input())
print(is_leap(year))