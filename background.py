import pygame
from pygame.sprite import Sprite
from Attributes import Attributes, Colors
w = Attributes["width"]
h = Attributes["height"]
fps = Attributes["fps"]

screen = pygame.display.set_mode((w, h))



class Background(Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("stars.png").convert_alpha()
        self.rect = self.image.get_rect()



    def update(self):

        clock = pygame.time.Clock()

        bgOne = self.image
        bgTwo = self.image

        bgOne2 = 0
        bgTwo2 = bgOne.get_width()


        screen.blit(bgOne, (bgOne2, 0))
        screen.blit(bgTwo, (bgTwo2, 0))

        pygame.display.update()

        bgOne2 -= 1
        bgTwo2 -= 1

        if bgOne2 == -1 * bgOne.get_width():
            bgOne2 = bgTwo2 + bgTwo.get_width()
        if bgTwo == -1 * bgTwo.get_width():
            bgTwo2 = bgOne2 + bgOne.get_width()
        
        clock.tick(30)

        