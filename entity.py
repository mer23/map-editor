from pygame.sprite import Sprite

class Character(Sprite):

	def __init__(self, image= None, heading= Entity.SOUTH):

		pygame.sprite.Sprite.__init__(self)
		self.image= image
		self.heading= heading



	def move(self, heading):
		pass


	def __str__(self):
		return super(Character).__str__() + "heading: " + Entity.str_cardinals[self.heading]



#############################################################################################



class Item(Sprite):

	def __init__(self, image= None):

		pygame.sprite.Sprite.__init__(self)
		self.image= image