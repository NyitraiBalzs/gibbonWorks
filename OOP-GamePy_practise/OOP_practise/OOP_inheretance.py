class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'I am {self.name} and i am {self.age} old!')

    def speak(self):
        print('I dont know what to say')


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def show(self):
        print(f'I am {self.name} and i am a {self.age} years old {self.color} cat!')

    def speak(self):
        print('meow')


class Dog(Pet):
    def __init__(self, name, age, type):
        super().__init__(name, age)
        self.type = type

    def show(self):
        print(f'I am {self.name} and i am a {self.age} years old {self.type} dog!')

    def speak(self):
        print('bark')


cat = Cat('tita', 4, 'cirmos')
dog = Dog('doge', 7, 'corgy')
pet = Pet('anyád', 9)

dog.show()
cat.show()
pet.show()