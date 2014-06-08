

class Tile(object):
	"""Represents a single tile in the map. 

	Attributes: surface, entities ."""

	def __init__(self, layers, entities = [], blocked = False, jump_over = False):
		self.layers = layers
		self.entities = entities
		self.blocked = blocked
		self.jump_over = jump_over

	def __str__(self):

		return (" || layers: " + self.layers +
				" || sprite: " + self.entity + "\n"
				"blocked: " + self.blocked +
				" || jump_over: " + self.jump_over + "\n")

