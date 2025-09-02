### Функції

def fun(a, b):
	c = a + b
	return c
	
def fun2(a: int) -> int:  # з поясненням якого типу будуть значкння
	c = a ** 2
	return c
	
d = fun2(3)
g = fun(3, 5)

print('val ', d)
print('val2 ', g )


# перевантаження 
# Приклад 1

def fun(a, b=None):
    if b is None:
        return a ** 2   # якщо передано тільки a
    else:
        return a + b    # якщо передано a і b

d = fun(3)
g = fun(3, 5)

print('val ', d)
print('val2 ', g)



# перевантаження 
# Приклад 2

def fun(*args):
    if len(args) == 1:
        a = args[0]
        return a ** 2
    elif len(args) == 2:
        a, b = args
        return a + b
    else:
        raise TypeError("fun() приймає 1 або 2 аргументи")

d = fun(3)
g = fun(3, 5)

print('val ', d)
print('val2 ', g)

