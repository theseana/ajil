file = open('names.txt', 'r')
for line in file:
    if 'amir' in line:
        print(line)