import math

x = 5.3
print(math.ceil(x))  # Output: 6
print(math.floor(x))  # Output: 5

x = 5
print(math.ceil(x))  # Output: 5
print(math.floor(x))  # Output: 5

x = 5.0
y = -4.3
print(math.copysign(x, y))  # Output: -5.0
print(math.copysign(y, x))  # Output: 4.3
print(math.copysign(0, -1))  # Output: -0.0 
print(math.copysign(0, 1))   # Output: 0.0
print(math.copysign(0, 0))   # Output: 0.0

x = -3.7
print(math.fabs(x))  # Output: 3.7

