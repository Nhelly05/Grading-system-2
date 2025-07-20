""" gading system by nhelly"""
def point(score):
    if score >= 70 and score <= 100:
        return 'A'
    elif score <= 69 and score >= 60:
        return 'B'
    elif score <= 59 and score >= 50:
        return 'C'
    elif score <= 49 and score >= 45:
        return 'D'
    elif score <= 44 and score >= 40:
        return 'E'
    else:
        return 'F'

name = input('Enter your name: ')
regNo = input('Enter your Matric number: ')
score = int(input('Enter Student score (0-100): '))
grade = point(score)

print(f'\nName: {name}')
print(f'Matric number: {regNo}')
print(f'your grade is: {grade}')
