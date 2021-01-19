name = input("Name: ")
last_name = input("LastName: ")

file = open('name_and_last_name.txt', 'a')
while name != 'end':
    txt = f"name: {name}, last_name: {last_name}\n" 
    file.write(txt)
    name = input("Name: ")
    last_name = input("LastName: ")
file.close()