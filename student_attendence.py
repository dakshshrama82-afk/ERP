import json
import student

with open("student_attendence.json","r") as f:
    data_stu = json.load(f)
a = 0
while True:
    print(student.student_names[a])
    name_student = student.student_names[a]
    prasent = input("student is (p/a): ")
    if prasent == "p":
            data_stu[name_student] +=1
    else:
        pass
    with open("","") as f:
         json.dump(data_stu,f)
    a += 1
    if a == 60:
        break
