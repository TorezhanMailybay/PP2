from math import *
n = int(input())
m = radians(n)
print(m)
h = int(input())
b1 = int(input())
b2 = int(input())
S = ((b1 + b2)/2)*h
print(S)
n = int(input())
l = int(input())
a = l/(2*tan(radians(180/n)))
A = (n * l * a) / 1/2
print(A)

