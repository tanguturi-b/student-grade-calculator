print("WELCOME TO STUDENT-GRADE-CALCULATOR")
name=input("enter your name:")
student_id=int(input("enter your student id:"))
python_marks=int(input("enter your python marks:"))
os_marks=int(input("enter your os marks:"))
dbms_marks=int(input("enter your dbms marks:"))
english_marks=int(input("enter your english marks:"))
maths_marks=int(input("enter your maths marks:"))
science_marks=int(input("enter your science marks:"))
print("====================================")
print("     STUDENT GRADE REPORT  ")
print("====================================")
print("Name:",name)
print("Student ID:",student_id)
print("Python Marks:",python_marks)
print("OS Marks:",os_marks)
print("DBMS Marks:",dbms_marks)
print("English Marks:",english_marks)
print("Maths Marks:",maths_marks)
print("Science Marks:",science_marks)
total_marks=python_marks+os_marks+dbms_marks+english_marks+maths_marks+science_marks
print("Total Marks:",total_marks)
Average=total_marks/6
print("Average Marks:",Average)
if Average>=90:
    print("Grade: A+")
elif Average>=80:
    print("Grade: A")
elif Average>=70:
    print("Grade: B")
elif Average>=60:
    print("Grade: C")
elif Average>=50:
    print("Grade: D")
else:
    print("Grade: F")

if Average>=50:
    print("Congratulations! You have passed the exam.")
else:
    print("Sorry! You have failed the exam. Better luck next time.")
