student={"Name":"Gayathri","Roll Number":21,"Register Number":10021,"Department":"Computer Science","Semester":1}
print(student)
total_mark=int(input("Enter The Mark:"))
student.update({"total_mark":total_mark})
total=student["total_mark"]
if total>=90:
    grade='A'
elif total>=82:
    grade='B'
elif total>=75:
    grade='C'
elif total>=60:
    grade='D'
elif total>=50:
    grade='P'
else:
    grade='F'
student.update({"grade":grade})
print(student)
del student["Roll Number"]
print(student)
