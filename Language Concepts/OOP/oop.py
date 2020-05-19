class Animal:
  def eat(self):
    print("food..yummy!")


class Dog(Animal):
  def __init__(self, name):
    self.name = name

  def speak(self):
    print("bark! My name is", self.name)


class Cat(Animal):
  def speak(self):
    print("meowww")


fido = Dog("fido")
fido.speak()
fido.eat()

buttons = Cat()
buttons.speak()
