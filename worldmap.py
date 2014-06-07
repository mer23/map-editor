

class Map(object):

	"""Represents a map in the world.


	Attributes: id, name, size, tiles"""

	def __init__(self, map_id, name, size=(0,0), tiles= []):
		self.id= map_id
		self.name= name
		self.size= size
		self.tiles= tiles


	def __str__(self):
		return "id: " + str(self.id) + " || name: " + self.name

