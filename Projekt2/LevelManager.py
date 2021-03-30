import math

import numpy as np
import pygame
from numpy.linalg import norm

from Projekt2.Brick import Brick
from Projekt2.levels.EndGameLevel import EndGameLevel
from Projekt2.levels.GameLevel import GameLevel


class LevelManager:

    def __init__(self, windowWidth, windowHeight, screen):
        self.screen = screen
        self.dummyBrick = Brick(0, 0)
        self.windowHeight = windowHeight
        self.windowWidth = windowWidth
        self.brickHeight = self.dummyBrick.rect.height
        self.brickWidth = self.dummyBrick.rect.width
        self.levels = self.generateLevels()

    def getMapLevel(self, level):
        switcher = {
            1: self.getFirstLevel(),
            2: self.getSecondLevel(),
            3: self.getThirdLevel(),
            4: self.getFourthLevel(),
            5: self.getFifthLevel()
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

    def getThirdLevel(self):
        bricks = pygame.sprite.Group()
        p1 = np.asarray([0, 0])
        p2 = np.asarray([self.windowWidth, self.windowHeight])
        p3 = np.asarray([0, self.windowHeight])
        p4 = np.asarray([self.windowWidth, 0])

        for i in range(100, self.windowWidth - 100, self.brickWidth):
            for j in range(100, self.windowHeight - 100, self.brickHeight):
                if (self.distanceFromLine(p1, p2, i, j) < 10
                        or self.distanceFromLine(p3, p4, i, j) < 10):
                    bricks.add(Brick(i, j))
        return bricks

    def getFourthLevel(self):
        bricks = pygame.sprite.Group()
        offset = 100
        p1 = np.asarray([offset, offset])
        p2 = np.asarray([offset, self.windowHeight - offset])
        p3 = np.asarray([self.windowWidth - offset, offset])
        p4 = np.asarray([self.windowWidth - offset, self.windowHeight - offset])
        for i in range(offset, self.windowWidth - offset + 1, self.brickWidth):
            for j in range(offset, self.windowHeight - offset + 1, self.brickHeight):
                if (self.distanceFromLine(p1, p2, i, j) < 10
                        or self.distanceFromLine(p1, p3, i, j) < 10
                        or self.distanceFromLine(p2, p4, i, j) < 10
                        or self.distanceFromLine(p3, p4, i, j) < 10):
                    bricks.add(Brick(i, j))
        return bricks

    def getFifthLevel(self):
        bricks = pygame.sprite.Group()
        eyePosition = [self.windowWidth / 3, self.windowHeight / 3]
        secondEyePosition = [self.windowWidth / 3 * 2, self.windowHeight / 3]

        for i in range(0, self.windowWidth, self.brickWidth):
            for j in range(int(self.windowHeight / 2), self.windowHeight, self.brickHeight):
                if abs(math.dist([i, j], [self.windowWidth / 2, self.windowHeight / 2])) < 150:
                    bricks.add(Brick(i, j))

        for i in range(0, self.windowWidth, self.brickWidth):
            for j in range(0, self.windowHeight, self.brickHeight):
                if 70 > math.dist([i, j], eyePosition) > 30:
                    bricks.add(Brick(i, j))

        for i in range(0, self.windowWidth, self.brickWidth):
            for j in range(0, self.windowHeight, self.brickHeight):
                if 70 > math.dist([i, j], secondEyePosition) > 30:
                    bricks.add(Brick(i, j))
        return bricks

    @staticmethod
    def distanceFromLine(lineStart, lineEnd, pointX, pointY):
        return np.abs(np.cross(lineEnd - lineStart, lineStart - np.asarray([pointX, pointY]))) / norm(
            lineEnd - lineStart)

    def getNextLevel(self):
        if len(self.levels) <= 0:
            pygame.quit()
        self.levels.pop(0)
        return self.levels[0]

    def generateLevels(self):
        levels = []
        for i in range(0, 6):
            levels.append(GameLevel(self.screen, self.getMapLevel(i)))
        levels.append(EndGameLevel(self.screen))
        return levels
