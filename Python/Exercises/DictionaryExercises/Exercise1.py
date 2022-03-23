students = []

print('====================')
print('  Students Average  ')
print('====================\n')

studentName = input('Write the name of student: ')
studentAverage = int(input('Write the average of student: '))

student = {
    studentName: {
        'average': studentAverage
    }
}

students.append(student)

print(student)
