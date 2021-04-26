import input
import output
import curses
import zipfile
import os

cu = curses.initscr()

def error(error):
    cu.addstr(error)
    cu.refresh()
    curses.napms(3000)
    cu.clear()
    cu.refresh()

class menu:
    students = []
    student_id = []
    snum = None
    courses = []
    course_id = []
    cnum = None
    marks = []
    if os.path.isfile('student.dat'):
        cu.addstr("Extracting...\n")
        zip_file = zipfile.ZipFile('student.dat', 'r')
        zip_file.extractall()
        if os.path.isfile('students.txt'):  # Load data from students.txt
            sf = open('students.txt', 'r').read().splitlines()
        if os.path.isfile('courses.txt'):  # Load data from courses.txt
            cf = open('courses.txt', 'r').read().splitlines()
        if os.path.isfile('marks.txt'):  # Load data from marks.txt
            mf = open('marks.txt', 'r').read().splitlines()
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
                input.Input.number_student(input, self)
                for i in range(self.snum):
                    input.Input.student_infor(input, self)
                cu.addstr("""
                (1) Input course information
                (2) Stop
                """)
                while True:
                    cu.addstr("--> What do you want to do next? ")
                    cu.refresh()
                    next_choice1 = cu.getstr().decode()
                    if next_choice1 == "1":
                        input.Input.number_course(input, self)
                        for i in range(self.cnum):
                            input.Input.course_infor(input, self)
                        break
                    elif next_choice1 == "2":
                        curses.endwin()
                        file_list = ['students.txt']
                        with zipfile.ZipFile('student.dat', 'w') as new_zip:
                            for file_name in file_list:
                                new_zip.write(file_name)
                            for file_name in file_list:
                                os.remove(file_name)
                        exit()
                    else:
                        error("Invalid choice!!! Please choose again\n")
                break
            elif choice1 == "2":
                input.Input.number_course(input, self)
                for i in range(self.cnum):
                    input.Input.course_infor(input, self)
                cu.addstr("""
                (1) Input student information
                (2) Stop
                """)
                while True:
                    cu.addstr("--> What do you want to do next? ")
                    cu.refresh()
                    next_choice2 = cu.getstr().decode()
                    if next_choice2 == "1":
                        input.Input.number_student(input, self)
                        for i in range(self.snum):
                            input.Input.student_infor(input, self)
                        break
                    elif next_choice2 == "2":
                        curses.endwin()
                        file_list = ['courses.txt']
                        with zipfile.ZipFile('student.dat', 'w') as new_zip:
                            for file_name in file_list:
                                new_zip.write(file_name)
                            for file_name in file_list:
                                os.remove(file_name)
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
        input.Input.mark_infor(input, self)

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
                output.Output.print_student(output, self)
            elif choice2 == "2":
                output.Output.print_course(output, self)
            elif choice2 == "3":
                output.Output.print_mark(output, self)
            elif choice2 == "4":
                output.Output.gpa(output, self)
            elif choice2 == "5":
                output.Output.sort_gpa(output, self)
            elif choice2 == "6":
                curses.endwin()
                file_list = ['students.txt', 'courses.txt', 'marks.txt']
                with zipfile.ZipFile('student.dat', 'w') as new_zip:
                    for file_name in file_list:
                        new_zip.write(file_name)
                    for file_name in file_list:
                        os.remove(file_name)
                exit()
            else:
                error("Invalid choice!!! Please choose again\n")

