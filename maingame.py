import pygame

pygame.init()
pygame.display.set_caption("")


background_sfx = pygame.mixer.Sound("Music.mp3")
background_sfx.play()
pygame.quit()