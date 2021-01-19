grades = []
total = 0

for i in range(5):
    grade = input('Enter your grade: ')
    total = total + float(grade)
    grades.append(grade)

print(f'Total: {total}')
print(f'Grades: {grades}')
print(f'Average: {total/5}')