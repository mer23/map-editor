from abc import ABCMeta, abstractmethod

class Entity(object):

	__metaclass__ = ABCMeta

	NORTH= 1
	WEST= 2
	SOUTH= 3
	EAST= 4

	str_cardinals= ["no", "north", "west", "south", "east"]

	def __init__(self, sprite= 0, jump_over= ()):
		self.sprite= sprite
		self.jump_over= jump_over

	@abstractmethod
	def abstr(self):
		pass

	def __str__(self):

		jump= ""
		if self.jump_over: 
			jump= "can be jumped over from: "
			for cardinal in self.jump_over:
				jump += Entity.str_cardinals[cardinal]+ " " #wtf
		else: jump= "can be jumped over: NO"

		return "id: " + str(self.sprite) + "\n" + jump + "\n"



#############################################################################################



class Character(Entity):


	def __init__(self, sprite= 0, jump_over= (), heading= Entity.SOUTH):

		self.heading= heading
		super(Character, self).__init__(sprite, jump_over)

	def abstr(self):
		pass

	def move(self, heading):
		pass


	def __str__(self):
		return super(Character).__str__() + "heading: " + Entity.str_cardinals[self.heading]



#############################################################################################



class Item(Entity):

	def abstr(self):
		pass