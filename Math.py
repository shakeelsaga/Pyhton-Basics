import math

x = 5.3
print(math.ceil(x))
print(math.floor(x))

x = 5
print(math.ceil(x))
print(math.floor(x))

x = 5.0
y = -4.3
print(math.copysign(x, y))  #
print(math.copysign(y, x))  
print(math.copysign(0, -1))  # 
print(math.copysign(0, 1))
print(math.copysign(0, 0))   

x = -3.7
print(math.fabs(x))  
