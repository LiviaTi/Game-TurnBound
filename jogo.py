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

	def receive_attack(self, damage):
		self.__life -= damage
		if self.__life < 0:
			self._life = 0

	def attack(self, target):
		damage = self.__level * 2
		target.receive_attack(damage)
		print(f"{self.get_name()} attack {target.get_name()} and caused {damage} damage")


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

class	Game:
	"""Game orchestrator class"""
	def __init__(self)->None:
		self.hero = Hero(name="Spider-Man", life=100, level=5, ability="spider sense")
		self.enemy = Enemy(name="Joker", life=80, level=4, kind="cheater")

	def start_battle(self):
		""" Manage the attle in turns """
		print("Starting battle:")
		while self.hero.get_life() > 0 and self.enemy.get_life() > 0:
			print("\n Character details:")
			print(self.hero.show_details())
			print(self.enemy.show_details())

			input("Press enter to attack...")
			choice = input("Choice (1 - Normal attack, 2 - Special attack):")

			if choice == '1':
				self.hero.attack(self.enemy)
			else:
				print("Invalid choice, choosen again")
		if self.hero.get_life() > 0:
			print("Congratulations you won the battle")
		else:
			print("You were defeated")
# Create game instance and start battle
jogo = Game()
jogo.start_battle()