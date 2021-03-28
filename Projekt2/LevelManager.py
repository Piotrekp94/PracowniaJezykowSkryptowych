import math

import pygame
from pygame.locals import KEYDOWN, K_ESCAPE, K_UP, K_DOWN, K_LEFT, K_RIGHT, QUIT

from Projekt2.Ball import Ball
from Projekt2.Brick import Brick
from Projekt2.Player import Player


class LevelManager:

    def __init__(self, windowWidth, windowHeight):
        self.dummyBrick = Brick(0, 0)
        self.windowHeight = windowHeight
        self.windowWidth = windowWidth
        self.brickHeight = self.dummyBrick.rect.height
        self.brickWidth = self.dummyBrick.rect.width

    def getMapLevel(self, level):
        switcher = {
            1: self.getFirstLevel()
        }
        return switcher.get(level)

    def getFirstLevel(self):
        bricks = pygame.sprite.Group()
        xoffset = 10
        amount = self.windowWidth / (self.brickWidth + xoffset)
        print(int(amount))
        for i in range(int(amount)):
            bricks.add(Brick(i * self.brickWidth + (i + 1) * xoffset + xoffset, 50))
        return bricks

    def getSecondLevel(self):
        bricks = pygame.sprite.Group()
        for i in range(0, self.windowWidth, self.brickWidth):
            for j in range(0, self.windowHeight, self.brickHeight):
                if abs(math.dist([i, j], [self.windowWidth / 2, self.windowHeight / 2])) < 150:
                    bricks.add(Brick(i, j))
        return bricks
