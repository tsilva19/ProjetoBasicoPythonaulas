class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def media_grades(self):
        return sum(self.grades) / len(self.grades)


student = Student("Bob", (100, 100, 93, 78, 90))

student2 = Student("Ralf", (90, 90, 93, 78, 90))


print(student2.name)
print(student2.media_grades())
