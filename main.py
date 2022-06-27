import json
class Arithmetic(object):
    def summarize(a, b):
        if (type(a) != int and type(b) != int):
            print("Not a number!")
        else:
            print(a+b)
    def subtract(a, b):
        if (type(a) != int and type(b) != int):
            print("Not a number!")
        else:
            print(a-b)
    def divide(a, b):
        if (type(a) != int and type(b) != int):
            print("Not a number!")
        else:
            if (a != 0 and b != 0):
                print(a/b)
            else:
                print("Cant divide by zero")
                if (a == 0):
                    print(1/b)
                else:
                    print(a/1)
    def multiply(a, b):
        if (type(a) != int and type(b) != int):
            print("Not a number!")
        else:
            print(a*b)
    def extent(a, b):
        if (type(a) != int and type(b) != int):
            print("Not a number!")
        else:
            print(a**b)

Arithmetic.summarize(2,3)
Arithmetic.subtract(1,2)
Arithmetic.multiply(1,2)
Arithmetic.divide(1,0)
Arithmetic.extent(1,2)

class Person(object):
    def __init__(self):
        self.name = ""
        self.age = 0
        self.gender = "M"
    
    def get_data(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")

class Student(Person):
    def __init__(self):
        self.specialization = ""
        self.course = ""

class Teacher(Person):
    def __init__(self):
        self.item = ""
        self.experience = ""

s1 = Student()
s1.name = "Иван"
s1.age = 18
s1.gender = "М"
s1.specialization = "Инженер"
s1.course = "Математика"
s1.get_data()
s2 = Student()
s2.name = "Степан"
s2.age = 20
s2.gender = "М"
s2.specialization = "Врач"
s2.course = "Химия"
s2.get_data()
s3 = Student()
s3.name = "Анна"
s3.age = 21
s3.gender = "Ж"
s3.specialization = "Программист"
s3.course = "Алгоритмы"
s3.get_data()

class Figure(object):
    def __init__(self, side_length):
        self.side_length = side_length
        self.side_count = 0
        self.parametr = self.side_length * self.side_count
    
    def get_data(self):
        print(f"Length: {self.side_length}, Count {self.side_count}, Parametr: {self.parametr}")

class Triangle(Figure):
    def __init__(self, side_length):
        self.side_length = side_length
        self.side_count = 3
        self.name = "Triangle"
        self.parametr = self.side_length * self.side_count
        self.square = (self.parametr * (self.parametr - self.side_length)) ** 0.5

    def get_data(self):
        print(f"Name: {self.name}, Length: {self.side_length}, Count {self.side_count}, Parametr: {self.parametr}, Square: {self.square}")

class Square(Figure):
    def __init__(self, side_length):
        self.side_length = side_length
        self.side_count = 4
        self.name = "Square"
        self.parametr = self.side_length * self.side_count
        self.square = self.parametr

    def get_data(self):
        print(f"Name: {self.name}, Length: {self.side_length}, Count {self.side_count}, Parametr: {self.parametr}, Square: {self.square}")

class Hexagon(Figure):
    def __init__(self, side_length):
        self.side_length = side_length
        self.side_count = 6
        self.name = "Hexagon"
        self.parametr = self.side_length * self.side_count
        self.square = (3 * (3 ** 0.5) * (self.side_length ** 2)) / 2

    def get_data(self):
        print(f"Name: {self.name}, Length: {self.side_length}, Count {self.side_count}, Parametr: {self.parametr}, Square: {self.square}")

t = Triangle(3)
s = Square(10)
h = Hexagon(5)

t.get_data()
s.get_data()
h.get_data()

class ContactBook(object):
    def __init__(self):
        self.full_name = ""
        self.phone_number = ""
        self.mail = ""
        self.bd = ""

    def jsonDownload(self):
        data = {}
        data["contats"] = []
        data["contats"].append({
            "FCs" : self.full_name,
            "Phone number" : self.phone_number,
            "Email" : self.mail,
            "Date of birth" : self.bd
        })

        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)

cb = ContactBook()
cb.full_name = "Ivanov Ivan Ivanovich"
cb.phone_number = "8 999 999 99 99"
cb.mail = "example@mail.ru"
cb.bd = "01.01.1970"

cb.jsonDownload()