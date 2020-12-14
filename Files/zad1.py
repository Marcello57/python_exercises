import os

dir = 'C:\\Users'
name = os.listdir(dir)
count = 0
for file in name:
    file_dir = '\\{}'.format(file)
    file_dir = dir + file_dir
    if os.path.isfile(file_dir):
        count += 1

print(count)
