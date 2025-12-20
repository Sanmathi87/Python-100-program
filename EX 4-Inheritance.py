class Student:
    def getStudentDetails(self):
        self.rollno = input("Enter Roll Number :")
        self.name = input("Enter Name :")
        self.physics = int(input("Enter Physics Marks :"))
        self.chemistry = int(input("Enter Chemistry Marks :"))
        self.maths = int(input("Enter Math Marks :"))

class SDetails(Student):
    def printResult(self):
        self.percentage = (int)((self.physics + self.chemistry + self.maths) / 300 * 100)
        print("Roll no:",self.rollno,"\nName:",self.name,"\nPercentage:",self.percentage)

S1 = SDetails()
S1.getStudentDetails()
print("Result:")
S1.printResult()

if (S1.percentage > 70):
    S1.physics += 9
    print("result after adding grace mark....")
    S1.printResult()
