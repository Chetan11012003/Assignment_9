# write a python script to print first N odd natural numbers in reverse order.

from re import I


n=int(input("Enter any number:- "))

i=2*n-1

while i>=1:
    print(i)
    i-=2