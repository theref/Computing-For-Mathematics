class Student():
	courses = ["Biology", "Mathematics", "English"]
	age = 12
	sex = 'Male'

	def haveabirthday(self, numberofbirthdays = 1):
		self.age += numberofbirthdays

vince = Student()
print vince.age
vince.haveabirthday()
print vince.age
vince.haveabirthday(28)
print vince.age
