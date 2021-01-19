number = input('Enter your number: ')
numbers = []
while number != '0':
    number = int(number)
    if number%2 == 1:
        numbers.append(number)
    number = input('Enter your number: ')
print(numbers)
average = sum(numbers)/len(numbers)
print(average)