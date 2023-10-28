import pygame
import sys
import os
from os import listdir
from os.path import isfile, join
import Player

pygame.init()

pygame.display.set_caption("Test game")

background_sfx = pygame.mixer.Sound("Music.mp3")
background_sfx.play()

#Variables for the game window dimensions
screen_w = 800
screen_h = 600
fps = 30
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
    __, __, width, height = image.get_rect()
    tiles = []

    for i in range (screen_w // width + 1):
        for j in range(screen_h // height + 1):
            pos = (i * screen_w, j * height)
            tiles.append(pos)
    return tiles, image 


def draw(window, background, bg_img):
    for tile in background:
        window.blit(bg_img, tile)
    pygame.display.update()


#Creating the game
def main(window):
    clock = pygame.time.Clock()
    background, bg_image = set_background("tempBG.png")

    game = True
    while game:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
        
        draw(window, background, bg_image)
        player.movement()
        player.jump()
    
        pygame.draw.rect(window, (255, 255, 255), (player.x, player.y, player.width, player.height))
        pygame.display.update()

    pygame.quit()
    quit()
    

if __name__ == "__main__":
    main(window)
