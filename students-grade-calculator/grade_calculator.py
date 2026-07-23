def calculate_grade(marks):
    if marks >= 90:
        return 'A', 'Excellent! Outstanding performance! 🌟'
    elif marks >= 80:
        return 'B', 'Very Good! Keep it up! 👍'
    elif marks >= 70:
        return 'C', 'Good effort! You can do even better! 😊'
    elif marks >= 60:
        return 'D', 'Keep practicing, improvement is possible! 💪'
    else:
        return 'F', 'Do not give up. Work hard and try again! 📚'

# Student name
name = input('Enter student name: ')

# Valid marks input
while True:
    try:
        marks = int(input('Enter marks (0-100): '))

        if 0 <= marks <= 100:
            break
        else:
            print('Marks must be between 0 and 100.')

    except:
        print('Please enter valid numbers only.')

# Calculate grade
grade, message = calculate_grade(marks)

# Display result
print('\n📊 RESULT FOR', name.upper())
print('Marks:', marks, '/100')
print('Grade:', grade)
print('Message:', message)