import pygame

from Projekt2.Ball import Ball
from Projekt2.Brick import Brick
from Projekt2.GameLoop import GameLoop
from Projekt2.Player import Player

pygame.init()


pygame.display.set_caption("Arkanoid UJ - Piechota Piotr")


def generate_level():
    pass


def update_ball_position():
    pass

pygame.mixer.music.load("sounds/intro.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

gameLoop = GameLoop(640, 480)

while gameLoop.isGameOn():
    gameLoop.mainLoop()

pygame.quit()
