# створили коротку функцію

a = 1
b = 2

shortFun1 = lambda x: x*2

shortFun2 = lambda x, y: x+y

shortFun3 = lambda x: "парне" if x % 2 == 0 else "непарне"

print(shortFun1(a))
print(shortFun2(a, b))
print(shortFun3(a))