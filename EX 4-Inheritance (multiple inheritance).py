
class Student:
    def getStudentDetails(self):
        self.rollno = input("Enter Roll Number : ")
        self.name = input("Enter Name : ")



class Marks:
    def getMarks(self):
        self.python = int(input("Enter Python Marks : "))
        self.java = int(input("Enter java Marks : "))
        self.maths = int(input("Enter Maths Marks : "))


class Result:
    def calculatePercentage(self):
        self.percentage = int((self.python + self.java + self.maths) / 300 * 100)



class SDetails(Student, Marks, Result):
    def printResult(self):
        output = (self.rollno, self.name, self.percentage)
        print(output)



S1 = SDetails()
S1.getStudentDetails()
S1.getMarks()
S1.calculatePercentage()

print("Result :")
S1.printResult()

if S1.percentage > 70:
    S1.python += 5
    S1.calculatePercentage()
    print("Result after adding grace marks...")
    S1.printResult()
