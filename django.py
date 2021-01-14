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
