class Student:
    def __init__(self, Student_management, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob
        Student_management.students.append(self)
        Student_management.student_id.append(self.__id)
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_dob(self):
        return self.__dob
class Student_management:
    students = []
    student_id = []
    snum = None
    def number_student(self):
        snum = int(input("\nThe total number of students is: "))
        while True:
            if snum <= 0:
                print("Invalid number!!! Please enter another number\n")
            else:
                break
        self.snum = snum
    def student_infor(self):
        print("\n** STUDENT INFORMATION **")
        while True:
            id = input("\tStudent ID: ")
            if id in self.student_id:
                print("This ID already existed. Please try another one\n")
            elif len(id) == 0:
                print("This cannot be empty. Please try again\n")
            else:
                break
        while True:
            name = input("\tStudent's name: ")
            if len(name) == 0:
                print("This cannot be empty. Please try again\n")
            else:
                break
        while True:
            dob = input("\tStudent's date of birth: ")
            if len(dob) == 0:
                print("This cannot be empty. Please try again\n")
            else:
                break
        Student(self, id, name, dob)
    def print(self):
        for student in self.students:
            print(f"\tID: {student.get_id()}, Name: {student.get_name()}, Date of birth: {student.get_dob()}")
class Course:
    def __init__(self, Course_management, id, name):
        self.__id = id
        self.__name = name
        Course_management.courses.append(self)
        Course_management.course_id.append(self.__id)
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
class Course_management:
    courses = []
    course_id = []
    cnum = None
    def number_course(self):
        cnum = int(input("\nThe total number of courses is: "))
        while True:
            if cnum <= 0:
                print("Invalid number!!! Please enter another number\n")
            else:
                break
        self.cnum = cnum
    def course_infor(self):
        print("\n** COURSE INFORMATION **")
        while True:
            id = input("\tCourse ID: ")
            if id in self.course_id:
                print("This ID already existed. Please try another one\n")
            elif len(id) == 0:
                print("This cannot be empty. Please try again\n")
            else:
                break
        while True:
            name = input("\tCourse's name: ")
            if len(name) == 0:
                print("This cannot be empty. Please try again\n")
            else:
                break
        Course(self, id, name)
    def print(self):
        for course in self.courses:
            print(f"\tID: {course.get_id()}, Name: {course.get_name()}")
class Mark:
    def __init__(self, Mark_management, cid, sid, mark):
        self.__cid = cid
        self.__sid = sid
        self.__mark = mark
        Mark_management.marks.append(self)
    def get_cid(self):
        return self.__cid
    def get_sid(self):
        return self.__sid
    def get_mark(self):
        return self.__mark
class Mark_management:
    marks = []
    def mark_infor(self):
        print("\n** MARK INPUT **")
        while True:
            cid = input("\tCourse ID: ")
            if cid in Course_management.course_id:
                for student in Student_management.students:
                    sid = student.get_id()
                    while True:
                        mark = float(input(f"\t{student.get_name()}'s mark: "))
                        if mark < 0:
                            print("Invalid value!!! Please do it again\n")
                        else:
                            break
                    Mark(self, cid, sid, mark)
            else:
                print("This course doesn't exist.\n")
            mark_choice = input("\nDo you want to choose another course? ")
            if mark_choice == "no":
                break
            elif mark_choice == "yes":
                print("Great! Here you go\n")
            else:
                print("Wrong choice!!! Let's choose again")
    def print(self):
        cid = input("\nPlease choose the course ID that you want to see mark: ")
        for course in Course_management.courses:
            if course.get_id() == cid:
                course_name = course.get_name()
                print(f"\t\tCourse name: {course_name}")
        for mark in self.marks:
            if mark.get_cid() == cid:
                sid = mark.get_sid()
                for student in Student_management.students:
                    if student.get_id() == sid:
                        print(f"\tFull name: {student.get_name()}, ID: {student.get_id()}, Mark: {mark.get_mark()}")
class menu:
    s = Student_management()
    c = Course_management()
    m = Mark_management()
    def engine(self):
        print("\tFUNCTION MENU")
        print("""
        (1) Input student information
        (2) Input course information
        (3) Stop
        """)
        while True:
            choice1 = input("\n--> You choose: ")
            if choice1 == "1":
                self.s.number_student()
                for i in range(self.s.snum):
                    self.s.student_infor()
                print("""
                (1) Input course information
                (2) Stop
                """)
                while True:
                    next_choice1 = input("--> What do you want to do next? ")
                    if next_choice1 == "1":
                        self.c.number_course()
                        for i in range(self.c.cnum):
                            self.c.course_infor()
                        break
                    elif next_choice1 == "2":
                        exit()
                    else:
                        print("Invalid choice!!! Please choose again\n")
                break
            elif choice1 == "2":
                self.c.number_course()
                for i in range(self.c.cnum):
                    self.c.course_infor()
                print("""
                (1) Input student information
                (2) Stop
                """)
                while True:
                    next_choice2 = input("--> What do you want to do next? ")
                    if next_choice2 == "1":
                        self.s.number_student()
                        for i in range(self.s.snum):
                            self.s.student_infor()
                        break
                    elif next_choice2 == "2":
                        exit()
                    else:
                        print("Invalid choice!!! Please choose again\n")
                break
            elif choice1 == "3":
                exit()
            else:
                print("Please choose again\n")
        self.m.mark_infor()
        print("\n\tFUNCTION MENU")
        print("""
        (1) Display all students
        (2) Display all courses
        (3) Display marks
        (4) Stop
        """)
        while True:
            choice2 = input("\n--> You choose: ")
            if choice2 == "1":
                self.s.print()
            elif choice2 == "2":
                self.c.print()
            elif choice2 == "3":
                self.m.print()
            elif choice2 == "4":
                exit()
            else:
                print("Invalid choice!!! Please choose again\n")
p = menu()
p.engine()





