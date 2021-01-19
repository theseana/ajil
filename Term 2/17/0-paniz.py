name = input('Enter name: ')
last_name = input('Enter last name: ')



file = open('write_name.txt', 'a')
while name != 'end':
    txt = f'name: {name} , last name: {last_name}\n'
    file.write(txt)
    name = input('Enter name: ')
    last_name = input('Enter last name: ')
file.close()

file = open('write_name.txt', 'r')
name = input('Enter your name for search: ')
for line in file:
    if name in line:
        (line)