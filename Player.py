import pygame

class Player:

    def __init__(self, x = 400, y = 400, width = 30, height = 30, move = 5, jumping = False, distance = 8, jumpCount = 8):
        #Player Details
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.move = move

        # Jumping
        self.jumping = jumping
        self.distance = distance
        self.jumpCount = jumpCount

    # Left and Right movement
    def movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.move
        if keys[pygame.K_RIGHT] and self.x < 800-self.width:
            self.x += self.move 
        
    # Jumping
    def jump(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.jumping = True
        if self.jumping:
            if self.jumpCount >= -1*self.distance:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= (self.jumpCount ** 2) * 0.5 * neg
                self.jumpCount -= 1
            else:
                self.jumping = False
                self.jumpCount = self.distance
    
