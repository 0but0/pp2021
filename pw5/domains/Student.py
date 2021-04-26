# For students
class Student:
    def __init__(self, menu, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob
        menu.students.append(self)
        menu.student_id.append(self.__id)

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob