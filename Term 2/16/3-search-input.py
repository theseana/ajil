name = input('Enter name to search:')
file = open('names.txt', 'r')
for line in file:
    if name in line:
        print(line)