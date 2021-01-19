search = input("search aLpHa name>>> ")
file = open("dar_hal_khandan.txt", "r")
for line in file:
    if search in line:
        print(line)