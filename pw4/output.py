# import main
import curses
import numpy as np
import math

cu = curses.initscr()

def error(error):
    cu.addstr(error)
    cu.refresh()
    curses.napms(3000)
    cu.clear()
    cu.refresh()

class Output:
    def print_student(self, menu):
        for student in menu.students:
            cu.addstr(f"\tID: {student.get_id()}, Name: {student.get_name()}, Date of birth: {student.get_dob()}")
            cu.refresh()

    def print_course(self, menu):
        for course in menu.courses:
            cu.addstr(f"\tID: {course.get_id()}, Name: {course.get_name()}, Credits: {course.get_credit()}")
            cu.refresh()

    def gpa(self, menu):
        all_marks = np.array([])
        all_credits = np.array([])
        while True:
            cu.addstr("Please enter a student ID that you want to see GPA: ")
            cu.refresh()
            sid = cu.getstr().decode()
            if sid in menu.student_id:
                for student in menu.students:
                    stuname = student.get_name()
                    for mark in menu.marks:
                        if mark.get_sid() == sid:
                            for course in menu.courses:
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

    def sort_gpa(self, menu):
        all_marks = np.array([])
        all_credits = np.array([])
        sort_student = []
        for student in menu.students:
            sid = student.get_id()
            sname = student.get_name()
            for mark in menu.marks:
                if mark.get_sid() == sid:
                    for course in menu.courses:
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


    def print_mark(self, menu):
        cu.addstr("\nPlease choose the course ID that you want to see mark: ")
        cu.refresh()
        cid = cu.getstr().decode()
        for course in menu.courses:
            if course.get_id() == cid:
                course_name = course.get_name()
                cu.addstr(f"\t\tCourse name: {course_name}")
                cu.refresh()
        for mark in menu.marks:
            if mark.get_cid() == cid:
                sid = mark.get_sid()
                for student in menu.students:
                    if student.get_id() == sid:
                        cu.addstr(f"\tFull name: {student.get_name()}, ID: {student.get_id()}, Mark: {mark.get_mark()}")
                        cu.refresh()
