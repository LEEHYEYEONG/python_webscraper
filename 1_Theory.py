# data types

a_string = "like this"
a_number = 3
a_float = 3.12
a_boolean = False
a_none = None


# list

days = ["Mon","Tue","Wed","Thur","Fri"]

print("Mon" in days)
print("Man" in days)
print(days[3])
print(len(days))

print(days)
days.append("Sat")
print(days)

days.reverse()
print(days)


# tuples and dicts

days =("Mon","Tue","Wed","Thur","Fri")

print(type(days))


hyeyeong = {
    "name":"Hyeyeong",
    "age" : 22,
    "korean" : True,
    "fav_food" : ["Chicken"]
}

print(hyeyeong)
print(hyeyeong["name"])
hyeyeong["pretty"] = True
print(hyeyeong)


# built in functions

print(len("dlksnfklsnd"))

age = "18"
print(type(age))
n_age = int(age)
print(type(n_age))


# creating function

# 파이선은 들여쓰기로 구분

# 함수 만들기

def say_hello():
    print("hello")

say_hello() # 함수 실행 


# function arguments

def say_hello(who):
    print("hello", who)

say_hello("hyeyeong")

def plus(a,b):
    print(a+b)

def minus(a, b=0): # 디폴트 값 설정
    print(a-b)

plus(2,5)
minus(2)
minus(2,5)


# returns

def p_plus(a,b):
    print(a+b)

def r_plus(a,b):
    return a+b    # return 은 함수를 종료

p_result = p_plus(2, 3)
r_result = r_plus(2, 3)

print(p_result, r_result)


# keyworded arguments

def plus(a,b):
    return a+b

result = plus(b=30, a=1)
print(result)

def say_hello(name,age):
    return f"Hello {name} you are {age} years old"   # 문자열끼리 +로 합칠 수도 있음


hello = say_hello(age="22", name="hyeyeong")
print(hello)


# conditionals

def plus(a,b):
    if type(b) is str:
        return None
    else:
        return a+b

print(plus(12,"10"))


def plus(a,b):
    if type(b) is int or type(b) is float:
        return a+b
    else:
        return None

print(plus(12,1.2))


# if else and or

def age_check(age):
    print(f"you are {age}")
    if age < 18:
        print("you can't drink")
    elif age == 18:
        print("you are new to this!")
    else:
        print("enjoy your drink")

age_check(18)


# for in

days = ("Mon", "Tue", "Wed", "Thu", "Fri")

for day in days:
  print(day)

for x in [1,2,3,4,5]:
  print(x)

for day in days:
  if day is "Wed":
    break
  else:
    print(day)

for letter in "hyeyeong":
    print(letter)


# modules

# 쓸 것만 import 
#import math

from math import ceil, fsum, fabs  # 특정함수만 가져올 때 from

# from math import fsum as sexy_sum fsum을 sexy_sum으로 정의하여 사용할 수 있음

print(ceil(1.2))  # ceil은 올림
print(fabs(-1.2))  # 절대값
print(fsum([1,2,3,4,5]))

from calculator import plus, minus  # from 파일명 

print(plus(1,2))
print(minus(1,2))

# print는 어떻게 무한히 인자를 받아올 수 있나??


