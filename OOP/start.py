class Dog:
	def __init__(self, age, hels):
		self.age = age
		self.hels = hels
		self.bomb = 10
		self.__shet = 15
	
	def getShet(self):
		return self.__shet
		
	def setShet(self, a):
		self.__shet = a
		
	def gaw(self):
		print(f'Гав')
		
	def show_age(self):
		print(f'Мені {self.age} років!')
		
		
lavrik = Dog(8, 55)

lavrik.show_age()

lavrik.age = 12

print(lavrik.getShet())
	
	