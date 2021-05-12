import math
import curses
from domains.Student import *
from domains.Course import *
from domains.Mark import *

cu = curses.initscr()

def error(error):
    cu.addstr(error)
    cu.refresh()
    curses.napms(3000)
    cu.clear()
    cu.refresh()

class Input:
    def number_student(self, menu):
        while True:
            cu.addstr("\nThe total number of students is: ")
            cu.refresh()
            snum = int(cu.getstr().decode())
            if snum <= 0:
                error("Invalid number!!! Please enter another number\n")
            else:
                break
        menu.snum = snum

    def student_infor(self, menu):
        cu.addstr("\n** STUDENT INFORMATION **\n")
        while True:
            cu.addstr("\tStudent ID: ")
            cu.refresh()
            id = cu.getstr().decode()
            if id in menu.student_id:
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
        if len(menu.students) == 0:
            f = open("students.txt", "w")
        else:
            f = open("students.txt", "a")
        f.write(id + "\t" + name + "\t" + dob + "\n")
        f.close()
        Student(menu, id, name, dob)

    def number_course(self, menu):
        while True:
            cu.addstr("\nThe total number of courses is: ")
            cu.refresh()
            cnum = int(cu.getstr().decode())
            if cnum <= 0:
                error("Invalid number!!! Please enter another number\n")
            else:
                break
        menu.cnum = cnum

    def course_infor(self, menu):
        cu.addstr("\n** COURSE INFORMATION **\n")
        while True:
            cu.addstr("\tCourse ID: ")
            cu.refresh()
            id = cu.getstr().decode()
            if id in menu.course_id:
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
        if len(menu.courses) == 0:
            f = open("courses.txt", "w")
        else:
            f = open("courses.txt", "a")
        f.write(id + "\t" + name + "\t" + str(credit) + "\n")
        f.close()
        Course(menu, id, name, credit)

    def mark_infor(self, menu):
        cu.addstr("\n** MARK INPUT **\n")
        while True:
            cu.addstr("\tCourse ID: ")
            cu.refresh()
            cid = cu.getstr().decode()
            if cid in menu.course_id:
                for student in menu.students:
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
                    if len(menu.marks) == 0:
                        f = open("marks.txt", "w")
                    else:
                        f = open("marks.txt", "a")
                    f.write(sid + "\t" + cid + "\t" + str(mark) + "\n")
                    f.close()
                    Mark(menu, cid, sid, mark)
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



