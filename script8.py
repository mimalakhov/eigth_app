#First__________________________________________________________
'''  Написать класс “animals” (животные), который включает общие признаки и поведения животных. 
     От “animals” наследовать класс “mammals” (млекопитающие), который включает общие признаки и поведения млекопитающих. 
     От “mammals” наследовать “human” (человек), “cat”(кот), “dog”(собака), у каждого свои признаки и поведения
'''
# Класс имеет только одно поле - имя
class Animals:
    def __init__(self, name):
        self.name = name
    def say_name(self):
        print(self.name)

# Класс наследует Animals и добавляет новые поля - пол и возраст
class Mammals(Animals):
    def __init__(self, name, gender, age):
        super().__init__(name)
        self.gender = gender
        self.age = age
    def say_info(self):
        print(f'Hello, I am {self.name}, I am {self.age}, and I am {self.gender}')

# Класс наследует Mammals и добавляет новое поле - фамилия
class Human(Mammals):
    def __init__(self, name, gender, age, surname):
        super().__init__(name, gender, age)
        self.surname = surname
    def is_name(self, name):
        if (self.name == name):
            print("Yes, it is my name")
        else:
            print("No, it is not my name")

# Класс наследует Mammals и добавляет новое поле - цвет шерсти
class Cat(Mammals):
    def __init__(self, name, gender, age, color):
        super().__init__(name, gender, age)
        self.color = color
    def meow(self):
        print("Meow...")

# Класс наследует Mammals и добавляет новое поле - порода
class Dog(Mammals):
    def __init__(self, name, gender, age, breed):
        super().__init__(name, gender, age)
        self.breed = breed
    def woof(self):
        print("Woof!!!")

#Second_and_Third______________________________________________________________________
'''Написать класс “Student”, который наследует класс human, 
   у которого среди прочих признаков есть “Количество сданных дз”.
   Перегрузить операторы сравнения так, чтобы студенты сравнивались по количеству сданных ими дз. 
'''
class Student(Human):
    def __init__(self, name, gender, age, surname, homework):
        super().__init__(name, gender, age, surname)
        self.homework = homework
    def __cmp__(self, other):
        if (self.homework > other.homework):
            return 1
        elif (self.homework < other.homework):
            return -1
        else:
            return 0

Me = Student("Mikhail", "male", 19, "Malakhov", 9)
Other = Student("Other", "male", 19, "Student", 0)
print(Me.__cmp__(Other))

cat = Cat("Barsik", "male", 5, "white")
cat.say_info()
cat.meow()