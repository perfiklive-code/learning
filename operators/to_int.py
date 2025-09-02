def to_int(value: str) -> int:
    while True:
        try:
            return int(value)
        except ValueError:
            value = input('Це не ціле число!\nВведіть ще раз ')
            
            
vol = input('vol')


if to_int(vol) > 10:
	print('yes')