# ==========IMPORTANT IMPORTS===============

import pygame
from pygame.sprite import Group, groupcollide, spritecollide, collide_circle
import random
import os

# from button import Start_Button
from Player import Player
from Asteroid import Asteroid
from Bullet import Bullet
from Attributes import Attributes, Colors
w = Attributes["width"]
h = Attributes["height"]
f = Attributes["fps"]
from Draw import draw_text, draw_shield_bar

from background import Background, Background2, Background3, Background4, Background5



# ===========START THE GAME================

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Intergalactic Adventures of Pizza Cat")
clock = pygame.time.Clock()

running = False



# ===========GRAPHICS & SOUND======================

# background = pygame.image.load("test.png").convert_alpha()
# background_rect = background.get_rect()

shoot_sound = pygame.mixer.Sound("pew.wav")
expl_sounds = []
for snd in ['expl3.wav', 'expl6.wav']:
    expl_sounds.append(pygame.mixer.Sound(snd))


# =======SCARY MONSTERS AND NICE SPRITES==========

#all sprites
all_sprites = Group()
player = Player()

layer1 = Background()
layer2 = Background2()
layer3 = Background3()
layer4 = Background4()
layer5 = Background5()

bullets = Group()
asteroids = Group()

all_sprites.add(layer1,layer2,layer3,layer4,layer5, player)

#Monsters
def newAsteroid():
    a = Asteroid()
    all_sprites.add(a)
    asteroids.add(a)

for i in range(16):
    newAsteroid()

# bullets
def shoot(player):
        bullet = Bullet(player.rect.right, player.rect.centery)
        all_sprites.add(bullet)
        bullets.add(bullet)



# ===================================================START SCREEN==========================================
intro = True

pygame.mixer.music.load('Metroid.wav')
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play(loops=-1)
start = pygame.image.load("startScreen.jpg")

while intro:
    clock.tick(f)


    screen.blit(start, [0,0]) 

    for event in pygame.event.get():
    # check for closing window
        if event.type == pygame.QUIT:
            intro = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                running= True
                intro = False
    pygame.display.flip()            

score = 0


pygame.mixer.music.set_volume(0.6)


pygame.mixer.music.load('GameMusic.wav')
pygame.mixer.music.play(loops=-1)

# ===================================================GAME LOOP==========================================

while running == True:

    # keep loop running at the right speed
    clock.tick(f)

    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shoot(player)

    # Update
    all_sprites.update()
    

    # check to see if a bullet hit a mob
    hits = groupcollide(asteroids, bullets, True, True)
    for hit in hits:
        score += 10
        random.choice(expl_sounds).play()
        newAsteroid()

    # check to see if a mob hit the player
    hits = spritecollide(player, asteroids, True, collide_circle)

    for hit in hits:
        player.shield -= 10
        random.choice(expl_sounds).play()
        newAsteroid()

        if player.shield <= 0:
            running = False


    # Draw / render
  
    screen.fill(Colors["black"]) 
    # screen.blit(background, background_rect) 
    all_sprites.draw(screen)
  
    #player stats
    draw_text(screen, str(score), 30, w / 2, 10)
    draw_shield_bar(screen, 15, 15, player.shield)
    

    # *after* drawing everything, flip the display
    pygame.display.flip()

    
    

pygame.quit()