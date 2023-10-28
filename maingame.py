import pygame
import sys

pygame.init()

pygame.display.set_caption("")

background_sfx = pygame.mixer.Sound("Music.mp3")
background_sfx.play()

#Variables for the game window dimensions
screen_w = 800
screen_h = 600

#Important color codes as variables
background = (173, 216, 230)
ground = (0, 100, 0)


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

