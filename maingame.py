import pygame
import sys
import os
from os import listdir
from os.path import isfile, join
import Player

pygame.init()

pygame.display.set_caption("")

#Sound Effects
background_sfx = pygame.mixer.Sound("Music.mp3")
walking_sfx = pygame.mixer.Sound("walking.wav")
shooting_sfx = pygame.mixer.Sound("gunshot.mp3")
damaged_sfx = pygame.mixer.Sound("playerhurt.mp3")
monster_spawn_sfx = pygame.mixer.Sound("monsterdeath.wav")
monster_death_sfx = pygame.mixer.Sound("monsterdeath.wav")
background_sfx.play()

#Variables for the game window dimensions
screen_w, screen_h = 800, 600
fps = 60
velocity = 5

window = pygame.display.set_mode((screen_w, screen_h))

player = Player.Player()
    
def draw(self, win):
    win.blit(self.image (self.rect.x, self.rect.y))

def set_background(file): 
    #background = (173, 216, 230)
    #ground = (0, 100, 0)
    #window.fill(background)
    image = pygame.image.load(join("assets", file))
    x, y, width, height = image.get_rect()
    tiles = []

    for i in range (screen_w // width + 1):
        for j in range(screen_h // height + 1):
            pos = (i * screen_w, j * height)
            tiles.append(pos)
    return tiles, image 


def draw(window, background, bg_img):
    for tile in background:
        window.blit(bg_img, tile)


#Draw floor
floor = pygame.image.load("assets/Tilesets/TX Tileset Ground.png")
floor_rect = floor.get_rect()
floor_rect.topleft = (0, 515)

def draw_floor():
    window.blit(floor, floor_rect)
    offset = 93
    for i in range(8):
        floor_rect.topleft = (offset, 515)
        window.blit(floor, floor_rect)
        offset += 93
    offset = 93
    floor_rect.topleft = (0, 515)

#Creating the game
screen = pygame.display.set_mode((screen_w, screen_h))

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    screen.fill(background)

    create_ground = pygame.Rect(0, 500, screen_w, 100)
    pygame.draw.rect(screen, ground, create_ground)

    pygame.display.flip()


#When Game is exited
pygame.quit()
sys.exit()

