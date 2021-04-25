import math
import numpy as np
import curses

def error(error):
    cu.addstr(error)
    cu.refresh()
    curses.napms(3000)
    cu.clear()
    cu.refresh()


# For students
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
        cu.addstr("\nThe total number of students is: ")
        cu.refresh()
        snum = int(cu.getstr().decode())
        while True:
            if snum <= 0:
                error("Invalid number!!! Please enter another number\n")
            else:
                break
        self.snum = snum

    def student_infor(self):
        cu.addstr("\n** STUDENT INFORMATION **\n")
        while True:
            cu.addstr("\tStudent ID: ")
            cu.refresh()
            id = cu.getstr().decode()
            if id in self.student_id:
                error("This ID already existed. Please try another one\n")
            elif len(id) == 0:
                error("This cannot be empty. Please try again\n")
            else:
                break
        while True:
            cu.addstr("\tStudent's name: ")
            cu.refresh()
            name = cu.getstr().decode()
            if len(name) == 0:
                error("This cannot be empty. Please try again\n")
            else:
                break
        while True:
            cu.addstr("\tStudent's date of birth: ")
            cu.refresh()
            dob = cu.getstr().decode()
            if len(dob) == 0:
                error("This cannot be empty. Please try again\n")
            else:
                break
        Student(self, id, name, dob)

    def print(self):
        for student in self.students:
            cu.addstr(f"\tID: {student.get_id()}, Name: {student.get_name()}, Date of birth: {student.get_dob()}")
            cu.refresh()


# For courses
class Course:
    def __init__(self, Course_management, id, name, credit):
        self.__id = id
        self.__name = name
        self.__credit = credit
        Course_management.courses.append(self)
        Course_management.course_id.append(self.__id)

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_credit(self):
        return self.__credit


class Course_management:
    courses = []
    course_id = []
    cnum = None

    def number_course(self):
        cu.addstr("\nThe total number of courses is: ")
        cu.refresh()
        cnum = int(cu.getstr().decode())
        while True:
            if cnum <= 0:
                error("Invalid number!!! Please enter another number\n")
            else:
                break
        self.cnum = cnum

    def course_infor(self):
        cu.addstr("\n** COURSE INFORMATION **\n")
        while True:
            cu.addstr("\tCourse ID: ")
            cu.refresh()
            id = cu.getstr().decode()
            if id in self.course_id:
                error("This ID already existed. Please try another one\n")
            elif len(id) == 0:
                error("This cannot be empty. Please try again\n")
            else:
                break
        while True:
            cu.addstr("\tCourse's name: ")
            cu.refresh()
            name = cu.getstr().decode()
            if len(name) == 0:
                error("This cannot be empty. Please try again\n")
            else:
                break
        while True:
            cu.addstr("\tCourse's credits: ")
            cu.refresh()
            credit = int(cu.getstr().decode())
            if credit <= 0:
                error("Invalid number!!! Please try again\n")
            else:
                break
        Course(self, id, name, credit)

    def print(self):
        for course in self.courses:
            cu.addstr(f"\tID: {course.get_id()}, Name: {course.get_name()}, Credits: {course.get_credit()}")
            cu.refresh()


# For marks
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
        cu.addstr("\n** MARK INPUT **\n")
        while True:
            cu.addstr("\tCourse ID: ")
            cu.refresh()
            cid = cu.getstr().decode()
            if cid in Course_management.course_id:
                for student in Student_management.students:
                    sid = student.get_id()
                    while True:
                        cu.addstr(f"\t{student.get_name()}'s mark: ")
                        cu.refresh()
                        raw_mark = float(cu.getstr().decode())
                        mark = math.floor(raw_mark * 10) / 10
                        if mark < 0:
                            error("Invalid value!!! Please do it again\n")
                        else:
                            break
                    Mark(self, cid, sid, mark)
            else:
                error("This course doesn't exist.\n")
            cu.addstr("\nDo you want to choose another course? ")
            cu.refresh()
            mark_choice = cu.getstr().decode()
            if mark_choice == "no":
                break
            elif mark_choice == "yes":
                cu.addstr("Great! Here you go\n")
                cu.refresh()
            else:
                error("Wrong choice!!! Let's choose again")

    def gpa(self):
        all_marks = np.array([])
        all_credits = np.array([])
        while True:
            cu.addstr("Please enter a student ID that you want to see GPA: ")
            cu.refresh()
            sid = cu.getstr().decode()
            if sid in Student_management.student_id:
                for student in Student_management.students:
                    stuname = student.get_name()
                    for mark in self.marks:
                        if mark.get_sid() == sid:
                            for course in Course_management.courses:
                                if course.get_id() == mark.get_cid():
                                    all_marks = np.append(all_marks, mark.get_mark())
                                    all_credits = np.append(all_credits, course.get_credit())
                    gpa = np.dot(all_marks, all_credits) / np.sum(all_credits)
                    cu.addstr(f"{stuname}'s GPA is {gpa}")
                    cu.refresh()
                    break
                break
            else:
                error("Student ID doesn't exist. Please try again")

    def sort_gpa(self):
        all_marks = np.array([])
        all_credits = np.array([])
        sort_student = []
        for student in Student_management.students:
            sid = student.get_id()
            sname = student.get_name()
            for mark in self.marks:
                if mark.get_sid() == sid:
                    for course in Course_management.courses:
                        if course.get_id() == mark.get_cid():
                            all_marks = np.append(all_marks, mark.get_mark())
                            all_credits = np.append(all_credits, course.get_credit())
            gpa = np.dot(all_marks, all_credits) / np.sum(all_credits)
            new_student = (sid, sname, gpa)
            sort_student.append(new_student)
        dt = [("sid", "U100"), ("sname", "U100"), ("GPA", float)]
        np_sort_student = np.array(sort_student, dtype=dt)
        sorted_student_list = np.sort(np_sort_student, order="GPA")[::-1]
        cu.addstr('\n'.join(map(str, sorted_student_list)))
        cu.refresh()


    def print(self):
        cu.addstr("\nPlease choose the course ID that you want to see mark: ")
        cu.refresh()
        cid = cu.getstr().decode()
        for course in Course_management.courses:
            if course.get_id() == cid:
                course_name = course.get_name()
                cu.addstr(f"\t\tCourse name: {course_name}")
                cu.refresh()
        for mark in self.marks:
            if mark.get_cid() == cid:
                sid = mark.get_sid()
                for student in Student_management.students:
                    if student.get_id() == sid:
                        cu.addstr(f"\tFull name: {student.get_name()}, ID: {student.get_id()}, Mark: {mark.get_mark()}")
                        cu.refresh()


# For running the program
class menu:
    s = Student_management()
    c = Course_management()
    m = Mark_management()

    def begin(message):
        row, colum = cu.getmaxyx()
        Xrow = int(row / 3)
        Ycolumn = int(colum / 3)
        if message == "--- This is a Student management program ---":
            cu.addstr(Xrow, Ycolumn, message, curses.A_BLINK)
            cu.refresh()
        else:
            cu.addstr(Xrow, Ycolumn, message, curses.A_BOLD)
            cu.refresh()

    def engine(self):
        menu.begin("---Hello =D---")
        cu.refresh()
        curses.napms(1000)
        menu.begin("This is a Student management program ")
        cu.refresh()
        curses.napms(2000)
        cu.clear()
        cu.refresh()
        # INPUT INFORMATION FOR STUDENTS AND COURSES HERE
        cu.addstr("\tFUNCTION MENU")
        cu.addstr("""
        (1) Input student information
        (2) Input course information
        (3) Stop
        """)
        while True:
            cu.addstr("\n--> You choose: ")
            cu.refresh()
            choice1 = cu.getstr().decode()
            if choice1 == "1":
                self.s.number_student()
                for i in range(self.s.snum):
                    self.s.student_infor()
                cu.addstr("""
                (1) Input course information
                (2) Stop
                """)
                while True:
                    cu.addstr("--> What do you want to do next? ")
                    cu.refresh()
                    next_choice1 = cu.getstr().decode()
                    if next_choice1 == "1":
                        self.c.number_course()
                        for i in range(self.c.cnum):
                            self.c.course_infor()
                        break
                    elif next_choice1 == "2":
                        curses.endwin()
                        exit()
                    else:
                        error("Invalid choice!!! Please choose again\n")
                break
            elif choice1 == "2":
                self.c.number_course()
                for i in range(self.c.cnum):
                    self.c.course_infor()
                cu.addstr("""
                (1) Input student information
                (2) Stop
                """)
                while True:
                    cu.addstr("--> What do you want to do next? ")
                    cu.refresh()
                    next_choice2 = cu.getstr().decode()
                    if next_choice2 == "1":
                        self.s.number_student()
                        for i in range(self.s.snum):
                            self.s.student_infor()
                        break
                    elif next_choice2 == "2":
                        curses.endwin()
                        exit()
                    else:
                        error("Invalid choice!!! Please choose again\n")
                break
            elif choice1 == "3":
                curses.endwin()
                exit()
            else:
                error("Please choose again\n")

        # INPUT MARKS HERE
        curses.napms(3000)
        cu.clear()
        cu.refresh()
        self.m.mark_infor()

        # SHOW ALL INFORMATION HERE
        curses.napms(3000)
        cu.clear()
        cu.refresh()
        cu.addstr("\n\tFUNCTION MENU")
        cu.addstr("""
        (1) Display all students
        (2) Display all courses
        (3) Display marks
        (4) Display student's GPA
        (5) Display descending list of students in terms of GPA
        (6) Stop
        """)
        while True:
            cu.addstr("\n--> You choose: ")
            cu.refresh()
            choice2 = cu.getstr().decode()
            if choice2 == "1":
                self.s.print()
            elif choice2 == "2":
                self.c.print()
            elif choice2 == "3":
                self.m.print()
            elif choice2 == "4":
                self.m.gpa()
            elif choice2 == "5":
                self.m.sort_gpa()
            elif choice2 == "6":
                curses.endwin()
                exit()
            else:
                error("Invalid choice!!! Please choose again\n")


# MAIN
if __name__ == "__main__":
    cu = curses.initscr()
    p = menu()
    p.engine()