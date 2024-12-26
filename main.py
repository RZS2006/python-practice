class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_age(self, age):
        self.age = age
    
    def get_age(self):
        return self.age
    
    def hit(self):
        print('bro is geeking')
    
john = Person('John', 28)

john.set_age(78)
print(john.get_age())
john.hit()