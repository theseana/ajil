number = input('Enter your number: ')
numbers = []
while number != '0':
    numbers.append(int(number))
    number = input('Enter your number: ')
print(numbers)
average = sum(numbers)/len(numbers)
print(average)