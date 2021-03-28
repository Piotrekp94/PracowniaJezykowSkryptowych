import pygame
from pygame.locals import KEYDOWN, K_ESCAPE, K_UP, K_DOWN, K_LEFT, K_RIGHT, QUIT

from Projekt2.Ball import Ball
from Projekt2.Brick import Brick
from Projekt2.Player import Player


class GameLoop:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.isPlaying = True
        self.screen = pygame.display.set_mode([width, height])
        self.player = Player(305, 450, width)
        self.ball = Ball(315, 440)
        self.bricks = pygame.sprite.Group()
        self.bricks.add(Brick(20, 20))
        self.clock = pygame.time.Clock()

    def isGameOn(self):
        return self.isPlaying

    def next(self):
        self.handleInput()

        pressed_keys = pygame.key.get_pressed()
        self.player.update(pressed_keys)
        self.draw()
        if pygame.sprite.spritecollideany(self.ball, self.bricks):
            delete_klocek = pygame.sprite.spritecollideany(self.ball, self.bricks)
            delete_klocek.kill()
            # usuniecie klocka

        self.clock.tick(60)
        pygame.display.flip()

    def handleInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isPlaying = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.isPlaying = False

    def draw(self):
        self.screen.fill((0, 0, 0))
        for brick in self.bricks:
            self.screen.blit(brick.surf, brick.rect)
        self.screen.blit(self.player.surf, self.player.rect)
        self.screen.blit(self.ball.surf, self.ball.rect)
