# code challenge

def plus(a,b):
    try:
        return a+b
    except:
        return float(a)+float(b)
    
def minus(a,b):
    try:
        return a-b
    except:
        return float(a)-float(b)

def times(a,b):
    return float(a)*float(b)

def division(a,b):
    try:
        return a/b
    except:
        return float(a)/float(b)

def reminder(a,b):
    try:
        return a%b
    except:
        return float(a)%float(b)

def negation(a):
    return -float(a)

def power(a,b):
    try:
        return a**b
    except:
        return float(a)**float(b)

print(plus("10",10))
print(minus(10,"10"))
print(times("10",10))
print(division(10,"10"))
print(reminder("20",13))
print(negation("10"))
print(power("10",10))
