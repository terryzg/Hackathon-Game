import pygame
import sys

pygame.init()

pygame.display.set_caption("The Game")

#Sound Effects
background_sfx = pygame.mixer.Sound("Music.mp3")
walking_sfx = pygame.mixer.Sound("walking.wav")
shooting_sfx = pygame.mixer.Sound("gunshot.mp3")
damaged_sfx = pygame.mixer.Sound("playerhurt.mp3")
monster_spawn_sfx = pygame.mixer.Sound("monsterdeath.wav")
monster_death_sfx = pygame.mixer.Sound("monsterdeath.wav")
background_sfx.play()

#Variables for the game window dimensions
screen_w = 800
screen_h = 600

#Important color codes as variables
background = (173, 216, 230)
ground = (0, 100, 0)


#Creating the game
screen = pygame.display.set_mode((screen_w, screen_h))

# Backround and Health
font = pygame.font.Font(None, 36)
def text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))
BLACK = (0, 0, 0)
health = 10
run = True

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    health_text = font.render(f"Health: {health}", True, BLACK)
    screen.blit(health_text, (10, 10))
    pygame.display.update()
    screen.fill(background)

    create_ground = pygame.Rect(0, 500, screen_w, 100)
    pygame.draw.rect(screen, ground, create_ground)

#When Game is exited
pygame.quit()
sys.exit()

