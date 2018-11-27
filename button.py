import pygame
from Attributes import Attributes, Colors
w = Attributes["width"]
h = Attributes["height"]




class Start_Button(object):
    def __init__(self, screen):
        # print "Start Button"
        # get the screen, and save it to this object
        self.screen = screen
        # how big is the screen? We need a rect
        self.screen_rect = self.screen.get_rect()

        # Set the title Screen
        self.image = pygame.image.load("startScreen.jpg").convert_alpha()
        self.rect = self.image.get_rect
        

    def draw_button(self):
        self.screen.blit(self.image, [0, 0])
        
        # pygame.mixer.music.load('Metroid.wav')
        # pygame.mixer.music.set_volume(0.6)
        # pygame.mixer.music.play(loops=-1)
     