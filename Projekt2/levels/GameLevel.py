import pygame

from Projekt2.Ball import Ball
from Projekt2.Player import Player
from Projekt2.levels.Level import Level
from pygame.locals import K_UP, K_DOWN, K_RETURN, K_p, K_n


class GameLevel(Level):
    def __init__(self, screen, bricks):
        super(GameLevel, self).__init__(screen)
        self.player = Player(305, 450, self.width)
        self.ball = Ball(315, 440)
        self.bricks = bricks

    def nextLoop(self):
        if self.gameIsPaused is False:
            pressed_keys = pygame.key.get_pressed()
            self.player.update(pressed_keys)
            self.draw()
            if self.ball is not None:
                # self.handleCollision()
                self.ball.move()
        else:
            self.draw()
            # self.drawPausedText()

    def handleInput(self, key):
        if key == K_p:
            self.togglePause()
        if key == K_n:
            self.disactiveLevel()

    def draw(self):
        self.screen.fill((0, 0, 0))
        for brick in self.bricks:
            self.screen.blit(brick.surf, brick.rect)
        if self.player is not None:
            self.screen.blit(self.player.surf, self.player.rect)
        if self.ball is not None:
            self.screen.blit(self.ball.surf, self.ball.rect)

        # if self.currentLevel > 5:
        #     font = pygame.font.Font(pygame.font.get_default_font(), 30)
        #     text_surface = font.render('Thank you for playing', True, (155, 2, 155))
        #     text_rect = text_surface.get_rect(center=(self.width / 2, self.height / 3))
        #     self.screen.blit(text_surface, text_rect)
        #     text_surface = font.render('Your Score is: ', True, (155, 2, 155))
        #     text_rect = text_surface.get_rect(center=(self.width / 2, self.height / 3 * 2))
        #     self.screen.blit(text_surface, text_rect)
