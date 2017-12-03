#! /usr/bin/python3


class stu:
    count = 0
    __good_stu = 0

    def __init__(self, name):
        self.name = name
        stu.count += 1

    def pri(self):
        print(stu.count)


class class1(stu):
    def __init__(self, name, age):
        stu.__init__(self, name)
        self.age = age

    def pri(self):
        print("总人数:" + str(self.count))


a = stu("ljj")
b = stu("ljj")
c = class1("ljj", 22)

a.pri()
c.pri()
