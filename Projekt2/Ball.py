import pygame


class Ball(pygame.sprite.Sprite):

    def __init__(self, x, y):
        self.surf = pygame.Surface((5, 5))
        self.surf.fill((255, 255, 255))
        self.startingPos = (x, y)
        self.rect = self.surf.get_rect(center=self.startingPos)
        self.velocity = pygame.Vector2(-1, -2)

    def move(self):
        self.rect.move_ip(self.velocity)

    def bounceX(self):
        self.velocity = pygame.Vector2(self.velocity.x * -1, self.velocity.y)

    def bounceY(self):
        self.velocity = pygame.Vector2(self.velocity.x, self.velocity.y * -1)

    def goDown(self):
        self.velocity = pygame.Vector2(self.velocity.x, abs(self.velocity.y))

    def goUp(self):
        self.velocity = pygame.Vector2(self.velocity.x, abs(self.velocity.y) * -1)

    def reset(self):
        self.rect = self.surf.get_rect(center=self.startingPos)
        self.velocity = pygame.Vector2(-10, -10)
