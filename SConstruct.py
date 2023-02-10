#script.py
from roster import student_roster
from classroom_organizer import ClassroomOrganizer
import itertools
student_roster_iter = iter(student_roster)
y = ClassroomOrganizer()
#print(y.student_combination())
Student_Math_Science = y.get_students_with_subject("Math") + y.get_students_with_subject("Science")
print(Student_Math_Science)
print(list(itertools.combinations(Student_Math_Science, 4)))