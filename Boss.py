import pygame
from pygame.sprite import Sprite
import random
import os

from Attributes import Attributes, Colors
w = Attributes["width"]
h = Attributes["height"]

boss_img = pygame.image.load("boss.png").convert_alpha()

class Boss(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = boss_img
        self.image.set_colorkey(Colors["black"])
        self.rect = self.image.get_rect()
        
        self.rect.centery = h / 2
        self.rect.right = 10
        self.speedy = 10
        self.rect.y = random.randrange(0, h)
        self.health = 30

    def takeDamage(self, ammountOfDamage):
        self.health -= ammountOfDamage
        



