

class Tile(object):
	"""Represents a single tile in the map. 

	Attributes: surface, entities ."""

	def __init__(self, layers, entities=[], blocked=False, jump_over=(), trigger=None):
		self.layers = layers
		self.entities = entities
		self.jump_over = jump_over

		if jump_over:
			self.blocked = True
		else: 
			self.blocked= blocked
			
		self.trigger = trigger

	def __str__(self):

		return (" || layers: " + self.layers +
				" || sprite: " + self.entity + "\n"
				"blocked: " + self.blocked +
				" || jump_over: " + self.jump_over + "\n")

