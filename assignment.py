# modify 80 in to 89
student_marks =[60,70,80] 
student_marks[2]= "89"
print(student_marks)


#add a new value called 55(append the new list)
student_marks=[60,70,80]
student_marks.append(55)
print(student_marks)


# find the size of the list having apended item 55
print(len(student_marks))

#write a python program to sum of all items in the list
import math
student_marks=math.fsum(student_marks)
print(student_marks)


#alternative
student_marks=[60,70,80,55]
total_marks=sum(student_marks)
print(total_marks)


#wite a python function that takes two lists and return true if they have one common member
student_marks=(input("student_marks:"))
student_marks=(input("student_marks:"))
if 80 in student_marks:
    print("yes,60,70, common numbers")
else:
    print("no,60,70 doesnot exist")



