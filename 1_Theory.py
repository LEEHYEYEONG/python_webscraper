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




