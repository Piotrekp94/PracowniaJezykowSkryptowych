import pygame


class Ball(pygame.sprite.Sprite):

    def __init__(self, x, y):
        self.surf = pygame.Surface((5, 5))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center=(x, y))
        self.velocity = pygame.Vector2(-1, -2)

    def move(self):

        self.rect.move_ip(self.velocity)
