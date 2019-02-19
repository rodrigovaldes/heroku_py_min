
import os
# Print some statements
print('Hello World')

# Some calculations
n = 5
m = 4
t = n + m
print(t)

with open('something.txt', 'w') as file:
    file.write('whatever')
    print('saved file')
    print(os.getcwd())
    print('$$$$$$$$$$$$$$$')
    print(os.listdir())
    print('Yes, you did it! This is running!')
