from calendar import day_name
from socket import send_fds


class school:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # data += self

    def getName(self):
        return self.name

    def getAge(self):
        return self.age



s1 = school("krish", 11)
print(s1.age)
print(s1.name)