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
	
	def show_details(self):
		return f"Name: {self.get_name()} \n Life: {self.get_life()} \n Level: {self.get_level()}"

class Hero(Character):
	def __init__(self, name, life, level, ability)-> None:
		super().__init__(name, life, level)
		self.__ability = ability
	
	def get_ability(self):
		return self.__ability
	
	def show_details(self):
		return f"{super().show_details()} \n Ability: {self.get_ability()} \n"


class Enemy(Character):
	def __init__(self, name, life, level, kind)-> None:
		super().__init__(name, life, level)
		self.__kind = kind
	
	def get_kind(self):
		return self.__kind

	def show_details(self):
		return f"{super().show_details()} \n Kind: {self.get_kind()}\n"

hero = Hero(name="Spider-Man", life=100, level=5, ability="spider sense")
print(hero.show_details())

enemy = Enemy(name="Joker", life=80, level=4, kind="cheater")
print(enemy.show_details())