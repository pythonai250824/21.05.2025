from typing import override


class Person:

    # Encapsulation

    def __init__(self, name, age=0):
        self.name = name

        # 1
        self.__age = age  # protected, access via special methods

        self.__hidden = 1

    def year_gone_by(self):
        self.__age += 1

    # 2 getter
    # this is how to allow access to protected values
    @property
    def age(self):
        return self.__age

    # 3 setter
    @age.setter
    def age(self, value):
        if value >= 0:
            self.__age = value

    @override
    def __str__(self):
        return f"Person {self.name} age={self.__age}"

danny = Person('danny', 18)
print(danny.age)

danny.age = -10  # without setter this line will fail

danny.age = 20  # without setter this line will fail

print(danny)

# encapsulation
# 1 protected field no access from outside the class code -- __
# 2 protected field readonly, no write access from outside the class code - getter
# 3 protected field read and write with supervision -- setter

