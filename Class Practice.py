class Animal(object):
    def __init__(self, age, name=''):
        self.__age = age
        self.__name = name

    def __str__(self):
        return 'This is an animal'

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name


class Dog(Animal):
    def __init__(self, age, name='', breed=''):
        super().__init__(age, name)
        self.__breed = breed

    def __str__(self):
        return f'This dog is a {self.__breed} named {Animal.get_name(self)} and is {Animal.get_age(self)} years old'

    def get_breed(self):
        return self.__breed

    def say(self):
        print('Woof')


class Cat(Animal):
    def __init__(self, age, name='', breed=''):
        super().__init__(age, name)
        self.__breed = breed

    def __str__(self):
        return f'This cat is a {self.__breed} named {Animal.get_name(self)} and is {Animal.get_age(self)} years old'

    def get_breed(self):
        return self.__breed

    def say(self):
        print('Meow')

class Lizard(Animal):
    def __init__(self, age, name='', species=''):
        super().__init__(age, name)
        self.__species = species
    
    def __str__(self):
        return f'This lizard is a {self.__species} named {Animal.get_name(self)} and is {Animal.get_age(self)} years old'
    
    def get_species(self):
        return self.__species


dog = Dog(2, name='Bob', breed='beagle')
cat = Cat(1, name='Kat', breed='tiger')
generic = Animal(119, name='Joe')
print(dog)
print(cat)
print(generic)
