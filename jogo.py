class Character:
	def __init__(self, name, life, level)-> None:
		self.__name = name
		self.__life = life
		self.__level = level

	def get_name(self):
		return self.__name
	
	def get_life(self):
		return self.__life
	
	def get_level(self):
		return self.__level

class Hero(Character):
	def __init__(self, name, life, level, ability)-> None:
		super().__init__(name, life, level)
		self.__ability = ability
	
	def get_ability(self):
		return self.__ability

class Enemy(Character):
	def __init__(self, name, life, level, kind)-> None:
		super().__init__(name, life, level)
		self.__kind = kind
	
	def get_kind(self):
		return self.__kind