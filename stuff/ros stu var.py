import easy_gui

# Define the function to calculate if there are enough teachers


def enough_teachers(num_students, num_teachers):
    if num_teachers >= num_students/20:
        return True
    else:
        return False

# Ask the user for the number of students and teachers


num_students = easy_gui.integerbox("Enter the number of students:")
num_teachers = easy_gui.integerbox("Enter the number of teachers:")

# Calculate if there are enough teachers
if enough_teachers(num_students, num_teachers):
    message = f"There are enough teachers for {num_students} students."
else:
    message = f"There are not enough teachers for {num_students} students."

# Show the result to the user
easy_gui.msgbox(message)
