class Student():
	courses = ["Biology", "Mathematics", "English"]
	age = 12
	sex = 'Male'

vince = Student()
print vince.courses
print vince.age
print vince.sex

vince.courses.append("French")
print vince.courses
vince.age = 28
print vince.age
vince.sex = "M"
print vince.sex