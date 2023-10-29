import pygame

class Player:

    def __init__(self, x = 400, y = 485, width = 30, height = 30, move = 5, jumping = False, distance = 8, jumpCount = 8, jump_duration=2, max_health=5):
        #Player Details
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.move = move
        self.max_health = max_health
        self.health = max_health

        # Jumping
        self.jumping = jumping
        self.distance = distance
        self.jumpCount = jumpCount

    # Left and Right movement
    def movement(self):
        keys = pygame.key.get_pressed()
        self.direction: int

        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.x > 0:
            self.x -= self.move
            self.direction = 0
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.x < 800-self.width:
            self.x += self.move 
            self.direction = 1
        
    # Jumping
    def jump(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] or keys[pygame.K_w]:
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
    

    def draw_health_bar(self, win):
        health_bar_width = int((self.health / self.max_health) * self.width)
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y - 10, self.width, 5))
        pygame.draw.rect(win, (0, 255, 0), (self.x, self.y - 10, health_bar_width, 5))
