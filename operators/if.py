a =10

if a ==10:
	print('true')
else:
	print('folse')
	
# короткий вираз

print('true') if a == 10 else print('folse')


match a:
	case 1:
		print('folse')
	case 10:
		print('true')
	case _:
		print('невідома команда')
		
		

match a:
    case n if n < 0:
        print("Від’ємне число")
    case n if n == 10:
        print("trye")
    case n if n > 0:
        print("Додатне число")