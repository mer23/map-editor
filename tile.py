

class Tile(object):
	"""Represents a single tile in the map. 

	Attributes: map, x, y, surface, entity."""

	def __init__(self, worldmap, x= 0, y= 0, surface= None, entity= None):

		self.map= worldmap
		self.x= x
		self.y= y
		self.surface= surface
		self.entity= entity


	def __str__(self):

		return "position: " + str(self.pos()) + " || surface: " + self.surface + " || sprite: " + self.entity + "\n"


	def pos(self):
		return (self.map, self.x, self.y)