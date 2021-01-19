name = input('Enter name: ')

file = open('2-names.txt', 'a')
while name != 'end':
    file.write(name+'\n')
    name = input('Enter name: ')
file.close()
