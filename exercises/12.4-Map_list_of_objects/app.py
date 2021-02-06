import datetime


people = [
	{ "name": 'Joe', "birthDate": datetime.datetime(1989,10,24) },
	{ "name": 'Bob', "birthDate": datetime.datetime(1976,5,24) },
	{ "name": 'Erika', "birthDate": datetime.datetime(1990,6,12) },
	{ "name": 'Dylan', "birthDate": datetime.datetime(2002,12,14) },
	{ "name": 'Steve', "birthDate": datetime.datetime(2006,4,24) }
]


def calculateAge(birthDate):
    today = datetime.date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

name_list = list(map(lambda person:  ("Hello, my name is " + person["name"] + " and I am " + str(calculateAge(person["birthDate"])) + " years old") , people))
print(name_list)

