file = open('miveh.txt', 'w')
file.write('Lemon\n')
file.write('Watermelon\n')
file.write('Melon\n')
file.close()

file = open('miveh.txt', 'a')
file.write('Kiwi\n')
file.write('Banana\n')
file.write('Apple\n')
file.close()

file = open('miveh.txt', 'r')
for i in file:
    print(i)
file.close()

