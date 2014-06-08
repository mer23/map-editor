

class Tile(object):
	"""Represents a single tile in the map. 

	Attributes: map, x, y, surface, entity."""

	def __init__(self, x= 0, y= 0, surface= None, entity= None, blocked= False, jump_over= False):

		self.x= x
		self.y= y
		self.surface= surface
		self.entity= entity
		self.blocked= blocked
		self.jump_over= jump_over

	def __str__(self):

		return ("position: " + str(self.pos()) +
				" || surface: " + self.surface +
				" || sprite: " + self.entity + "\n"
				"blocked: " + self.blocked +
				" || jump_over: " + self.jump_over + "\n")


	def pos(self):
		return (self.map, self.x, self.y)