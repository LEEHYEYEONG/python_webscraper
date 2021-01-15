# *args, **kwargs

def plus(*args):
  result = 0
  for number in args:
    result += number
  return result


print(plus(3,3,3,3))


# Object Oriented Programming

class Car():
  wheels = 4
  doors = 4
  windows = 4
  seats = 4

porche = Car()
porche.color = "Red"

ferrai = Car()
ferrai.color = "Yellow"

mini = Car()
mini.color="White"


# Methods part one

class Car():
  wheels = 4
  doors = 4
  windows = 4
  seats = 4

  def start(self):
    print(self.doors)
    print("I started") # 메소드의 첫번째 argument는 메소드를 호출하는 instance 자신


porche = Car()
porche.start()


# Methods part two

class Car():
  wheels = 4
  doors = 4
  windows = 4
  seats = 4

  # kwargs 는 dictionary 자료구조
  def __init__(self, **kwargs):
    self.wheels = 4
    self.doors = 4
    self.windows = 4
    self.seats = 4
    self.color = kwargs.get("color", "black")
    self.price = kwargs.get("price", "$20")
  
  def __str__(self):
    return f"Car with {self.wheels} wheels"

# dir은 class 안에 있는 모든 것들을 리스트로 보여준다
# __str__은 그 class 의 instance를 출력

# print(dir(Car))

porche = Car(color = "green", price = "$40")
print(porche.color, porche.price) # __str__자동으로 호출

mini = Car()
print(mini.color, mini.price)


# Extending Classes

class Car():

  def __init__(self, **kwargs):
    self.wheels = 4
    self.doors = 4
    self.windows = 4
    self.seats = 4
    self.color = kwargs.get("color", "black")
    self.price = kwargs.get("price", "$20")
  
  def __str__(self):
    return f"Car with {self.wheels} wheels"

class Convertible(Car):

  def __init__(self, **kwargs):
    super.__init__(**kwargs)
    self.time = kwargs.get("time", 10)

  def take_off(self):
    return "taking off"

  def __str__(self):
    return f"Car with no roof"


porche = Car(color = "green", price = "$40")
print(porche.color)

mini = Car()


