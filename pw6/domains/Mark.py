# For marks
class Mark:
    def __init__(self, menu, cid, sid, mark):
        self.__cid = cid
        self.__sid = sid
        self.__mark = mark
        menu.marks.append(self)

    def get_cid(self):
        return self.__cid

    def get_sid(self):
        return self.__sid

    def get_mark(self):
        return self.__mark
