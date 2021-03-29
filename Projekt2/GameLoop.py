import pygame
from pygame.locals import KEYDOWN, K_ESCAPE, K_n

from Projekt2.Ball import Ball
from Projekt2.LevelManager import LevelManager
from Projekt2.Player import Player


class GameLoop:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.isPlaying = True
        self.screen = pygame.display.set_mode([width, height])
        self.player = Player(305, 450, width)
        self.ball = Ball(315, 440)

        self.levelManager = LevelManager(width, height)
        self.clock = pygame.time.Clock()
        self.currentLevel = 4
        self.bricks = self.levelManager.getMapLevel(self.currentLevel)

    def isGameOn(self):
        return self.isPlaying

    def next(self):
        self.handleInput()

        pressed_keys = pygame.key.get_pressed()
        self.player.update(pressed_keys)
        self.draw()
        self.handleCollision()
        self.ball.move()
        self.clock.tick(60)
        pygame.display.flip()

    def handleInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isPlaying = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.isPlaying = False
                if event.key == K_n:
                    self.loadNextLevel()

    def draw(self):
        self.screen.fill((0, 0, 0))
        for brick in self.bricks:
            self.screen.blit(brick.surf, brick.rect)
        self.screen.blit(self.player.surf, self.player.rect)
        self.screen.blit(self.ball.surf, self.ball.rect)

    def handleCollision(self):
        # collidingObject = pygame.sprite.spritecollideany(self.ball, self.bricks)
        # if (collidingObject):
        #     if(collidingObject.rect.width / 2):
        #
        #     collidingObject.kill()
        pass

    def loadNextLevel(self):
        if self.currentLevel < 6:
            self.currentLevel += 1
            self.bricks = self.levelManager.getMapLevel(self.currentLevel)
            self.ball = Ball(315, 440)
            print(self.currentLevel)
        if self.currentLevel >= 6:
            self.bricks = []
