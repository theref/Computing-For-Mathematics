class Student():
	def __init__(self, courses, age, sex):
		self.courses = courses
		self.age = age
		self.sex = sex

	def haveabirthday(self, numberofbirthdays):
		self.age += numberofbirthdays

vince = Student(["Biology","Math"], 28, "Male")
print vince.courses
print vince.age
print vince.sex