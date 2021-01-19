grades = []
total = 0
number = int(input('Enter your number: '))
for i in range(number):
    grade = input('Enter your grade: ')
    total = total + float(grade)
    grades.append(grade)

print(f'Total: {total}')
print(f'Grades: {grades}')
print(f'Average: {total/number}')