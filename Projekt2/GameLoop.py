import pygame
from pygame.locals import KEYDOWN, K_ESCAPE, K_n, K_p

from Projekt2.Ball import Ball
from Projekt2.LevelManager import LevelManager
from Projekt2.Player import Player


class GameLoop:

    def __init__(self, width, height):
        self.gameIsPaused = False
        self.width = width
        self.height = height
        self.isPlaying = True
        self.screen = pygame.display.set_mode([width, height])
        self.player = Player(305, 450, width)
        self.ball = Ball(315, 440)

        self.levelManager = LevelManager(width, height)
        self.clock = pygame.time.Clock()
        self.currentLevel = 1
        self.bricks = self.levelManager.getMapLevel(self.currentLevel)

    def isGameOn(self):
        return self.isPlaying

    def next(self):
        self.handleInput()
        if self.gameIsPaused is False:
            pressed_keys = pygame.key.get_pressed()
            self.player.update(pressed_keys)
            self.draw()
            if self.ball is not None:
                self.handleCollision()
                self.ball.move()
        else:
            self.draw()
            self.drawPausedText()
        self.clock.tick(60)
        pygame.display.flip()

    def handleInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isPlaying = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.isPlaying = False
                if event.key == K_n and not self.gameIsPaused:
                    self.loadNextLevel()
                if event.key == K_p:
                    self.gameIsPaused = not self.gameIsPaused

    def draw(self):
        self.screen.fill((0, 0, 0))
        for brick in self.bricks:
            self.screen.blit(brick.surf, brick.rect)
        if self.player is not None:
            self.screen.blit(self.player.surf, self.player.rect)
        if self.ball is not None:
            self.screen.blit(self.ball.surf, self.ball.rect)

        if self.currentLevel > 5:
            font = pygame.font.Font(pygame.font.get_default_font(), 30)
            text_surface = font.render('Thank you for playing', True, (155, 2, 155))
            text_rect = text_surface.get_rect(center=(self.width / 2, self.height / 3))
            self.screen.blit(text_surface, text_rect)
            text_surface = font.render('Your Score is: ', True, (155, 2, 155))
            text_rect = text_surface.get_rect(center=(self.width / 2, self.height / 3 * 2))
            self.screen.blit(text_surface, text_rect)

    def handleCollision(self):
        # collidingObject = pygame.sprite.spritecollideany(self.ball, self.bricks)
        # if (collidingObject):
        #     if(collidingObject.rect.width / 2):
        #
        #     collidingObject.kill()
        pass

    def loadNextLevel(self):
        if self.currentLevel < 5:
            self.bricks = self.levelManager.getMapLevel(self.currentLevel + 1)
            self.ball = Ball(315, 440)
        if self.currentLevel == 5:
            self.loadLastLevel()
        if self.currentLevel > 5:
            self.isPlaying = False
        self.currentLevel += 1

    def loadLastLevel(self):
        self.bricks = []
        self.ball = None

    def drawPausedText(self):
        font = pygame.font.Font(pygame.font.get_default_font(), 36)
        # now print the text
        text_surface = font.render('Paused', True, (155, 2, 155))
        text_rect = text_surface.get_rect(center=(self.width / 2, self.height / 2))
        self.screen.blit(text_surface, text_rect)
