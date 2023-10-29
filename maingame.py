import pygame
import sys
import os
from os import listdir
from os.path import isfile, join
import Player

pygame.init()

pygame.display.set_caption("Test game")

#Sound Effects
background_sfx = pygame.mixer.Sound("Music.mp3")
walking_sfx = pygame.mixer.Sound("walking.wav")
shooting_sfx = pygame.mixer.Sound("gunshot.mp3")
damaged_sfx = pygame.mixer.Sound("playerhurt.mp3")
monster_spawn_sfx = pygame.mixer.Sound("monsterdeath.wav")
background_sfx.set_volume(0.2)
background_sfx.play()

#Variables for the game window dimensions
screen_w, screen_h = 800, 600
fps = 60
velocity = 5

window = pygame.display.set_mode((screen_w, screen_h))

player = Player.Player()
    
def draw(self, win):
    win.blit(self.image (self.rect.x, self.rect.y))
    self.hitbox = (self.x + 15, self.y, 30, 10)
    pygame.draw.rect(win, (255, 0, 0), (self.x + 15, self.y, 30, 10))
    pygame.draw.rect(win, (255, 0, 0), (self.x + 15, self.y, 30, 10))
    pygame.draw.rect(win, (0, 0, 0), self.hitbox, 1)

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


font = pygame.font.Font(None, 36)
def text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    window.blit(img, (x,y))
BLACK = (0, 0, 0)
health = 10

#Creating the game
def main(window):
    clock = pygame.time.Clock()
    background, bg_image = set_background("testBG.png")

    game = True
    while game:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
        health_text = font.render(f"Health: {health}", True, BLACK)
        window.blit(health_text, (10, 10))
        pygame.display.update()
        draw(window, background, bg_image)
        player.movement()
        player.jump()
        draw_floor()
        pygame.draw.rect(window, (255, 255, 255), (player.x, player.y, player.width, player.height))
        player.draw_health_bar(window)


    pygame.quit()
    quit()
    

if __name__ == "__main__":
    main(window)
