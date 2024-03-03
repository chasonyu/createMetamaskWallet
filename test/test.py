import time

import os

my_file = open("userData/user.txt", "a")
my_file.write('wenben 1\n')
my_file.write('wenben 2\n')
my_file.write('wenben 3\n')
my_file.write('wenben 4\n')

my_file.close()



my_file = open("userData/user.txt", "r")
print(my_file.readlines())


