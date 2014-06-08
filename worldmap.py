

class Map(object):

    """Represents a map in the world.


    Attributes: id, desc, size, width, height, tiles"""

    def __init__(self, map_id, desc, size=(0,0), tiles= []):
        self.id= map_id
        self.desc= desc
        self.size= size
        self.width= size[0]
        self.height= size[1]
        self.tiles= tiles


    def __str__(self):
        return "id: " + str(self.id) + " || desc: " + self.name

