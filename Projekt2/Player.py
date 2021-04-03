import pygame
from pygame.locals import KEYDOWN, K_ESCAPE, K_UP, K_DOWN, K_LEFT, K_RIGHT, QUIT


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, width):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.Surface((30, 10))
        self.surf.fill((255, 0, 0))
        self.surf = pygame.image.load("images/belka.png").convert()
        self.rect = self.surf.get_rect(center=(x, y))
        self.screenWidth = width
        self.lifes = 3

    def update(self, pressed_keys):
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-3, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(3, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screenWidth - 30:
            self.rect.right = self.screenWidth - 30

    def getLifes(self):
        return self.lifes
