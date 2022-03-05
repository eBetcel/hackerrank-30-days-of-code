class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
    #   Function Name: calculate
    def calculate(self):
        total = 0
        for i in self.scores:
            total += i
        
        result = total / len(self.scores)
        
        if result >= 90 and result <= 100:
            return 'O'
        elif result >= 80 and result < 90:
            return 'E'
        elif result >= 70 and result < 80:
            return 'A'
        elif result >= 55 and result < 70:
            return 'P'
        elif result >= 40 and result < 55:
            return 'D'
        elif result < 40:
            return 'T'
    #   Return: A character denoting the grade.
    #
    # Write your function here

line = input().split()