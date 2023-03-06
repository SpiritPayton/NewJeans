"""GUI program to calculate if there is a sufficient number of teachers for the number of students at a school
"""
import easy_gui


def enough_teachers(school_roll, teacher_roll):
    if teacher_roll >= teacher_roll/class_roll:
        return True
    else:
        return False


school = easy_gui.enterbox("Enter the name of the Kura: ")
class_roll = easy_gui.integerbox("What is the max num of students allowed in a class?: "
                                 "(Must be a number between 10 and 30)", upperbound=30, lowerbound=10)
school_roll = easy_gui.integerbox(f"What is the total num of children at {school}", upperbound=1400, lowerbound=10)
teacher_roll = easy_gui.integerbox(f"How many teachers are at {school}", upperbound=120, lowerbound=1)


if enough_teachers(school_roll, teacher_roll):
    message = f"Good job!!!!!!! {school} has enough teachers for {school_roll} students."
else:
    message = f"{school} needs to hire some more teachers so that they can teach {school_roll} students."

# show results
easy_gui.msgbox(message)
