import pygame

from Projekt2.levels.GameLevel import GameLevel
from Projekt2.levels.Level import Level
from pygame.locals import K_UP, K_DOWN, K_RETURN


class EndGameLevel(GameLevel):
    def nextLoop(self):
        pressed_keys = pygame.key.get_pressed()
        self.player.update(pressed_keys)
        self.draw()

    def handleInput(self, key):
        pass

    def __init__(self, screen):
        super(EndGameLevel, self).__init__(screen, [])

    def draw(self):
        self.screen.fill((0, 0, 0))
        if self.player is not None:
            self.screen.blit(self.player.surf, self.player.rect)
        font = pygame.font.Font(pygame.font.get_default_font(), 30)
        text_surface = font.render('Thank you for playing', True, (155, 2, 155))
        text_rect = text_surface.get_rect(center=(self.width / 2, self.height / 3))
        self.screen.blit(text_surface, text_rect)
        text_surface = font.render('Your Score is: ', True, (155, 2, 155))
        text_rect = text_surface.get_rect(center=(self.width / 2, self.height / 3 * 2))
        self.screen.blit(text_surface, text_rect)
