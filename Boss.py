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

        self.radius = int(self.rect.width / 2)

        self.rect.x = 1400
        
        self.rect.y = h / 2
        self.speedx = 5

        
    def update():
        self.rect.x -= self.speedx
        self.image = boss_img
        if self.rect.x == 1000:
            self.rect.x == 1000

    


            