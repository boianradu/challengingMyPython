class Student():
    def __init__(self, name):
        self.name=name 
    def printStudent(self):
        print("Student name is:", self.name)
class StudentTax(Student):
    def __init__(self, name):
        super().__init__(name)
        self.tax=3000
    def printStudent(self):
        super().printStudent()
        print("And the tax is :", self.tax)
class StudentSuperTax(StudentTax):
    def __init__(self, name):
        super().__init__(name)
        self.superTax=55
        self.tip="Super taax"
    def printStudent(self):
        super().printStudent()
        print("And the super tax is :", self.superTax, self.tip)



st = StudentSuperTax("Dragos")
st.printStudent()
