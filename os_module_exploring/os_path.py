import os
from os import path

# Print the name of the os
print(os.name)

# Print the existance of a file and few others
print("Item Exists: " + str(path.exists('test.txt')))
print('Item is a File: ' + str(path.isfile('test.txt')))
print('Item is a Directory: ' + str(path.isdir('test.txt')))

# Get a files Full Path
print("Real Path of the File: " + str(path.realpath('test.txt')))

# Splite File name and the path
item, file_path = path.split(path.realpath('test.txt'))
print(item, file_path)
print("Item and Path name: ", str(path.split(path.realpath('test.txt'))))