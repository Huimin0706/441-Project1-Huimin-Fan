class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def __repr__(self):
        return self.__str__()

    # getters
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gpa(self):
        return self.gpa

    # setters
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_gpa(self, gpa):
        self.gpa = gpa

    # string
    def __str__(self):
        return "Student:\n\tname:" + self.name + "\n\tage:" + str(self.age) + "\n\tgpa:" + str(self.gpa)


