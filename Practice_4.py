"""
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird

"""

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

