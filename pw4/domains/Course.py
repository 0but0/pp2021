# For courses
class Course:
    def __init__(self, menu, id, name, credit):
        self.__id = id
        self.__name = name
        self.__credit = credit
        menu.courses.append(self)
        menu.course_id.append(self.__id)

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_credit(self):
        return self.__credit