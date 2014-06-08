from pygame.sprite import Sprite

class GroundSurface(Sprite):

    def __init__(self, image= None):

        pygame.sprite.Sprite.__init__(self)
        self.image= image
