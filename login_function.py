import student
import teacher
user = input("who is the user (student or teacher):").lower()


def login_student():
    a = True
    while a:
        user_name = input("enter the name:" )
        if user_name in student.student:
            password = input("enter the pass:")
            if student.student_pass[user_name] == password:
                user_id = input("enter the user id: ")
                if student.student[user_name] == user_id:
                    print("wellcome to the ERP")
                    a = False
                elif student.student[user_name] != user_id:
                    print("wrong user id tri again")
            elif student.student_pass[user_name] != password:
                print("wrong pass")
        elif True:
            print("wrong user name tri again")


def login_teacher():
    b = True
    while b:
        user_name = input("enter the name:" )
        if user_name in teacher.teacher:
            password = input("enter the pass: ")
            if teacher.teacher_pass[user_name] == password:
                user_id = input("enter the user id: ")
                if teacher.teacher[user_name] == user_id:
                    print("wellcome to the ERP")
                    b = False
                elif teacher.teacher[user_name] != user_id:
                    print("wrong user id tri again")
            elif teacher.teacher_pass[user_name] != password:
                print("wrong pass")
        elif True:
            print("wrong user name tri again")

if user == "student":
    login_student()
elif user == "teacher":
    login_teacher()
else:
    print("no option found")
