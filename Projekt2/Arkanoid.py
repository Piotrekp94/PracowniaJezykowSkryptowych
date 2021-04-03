import pygame

from Projekt2.GameLoop import GameLoop

pygame.init()

pygame.display.set_caption("Arkanoid UJ - Piechota Piotr")

pygame.mixer.music.load("sounds/intro.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)
open('leaderboard.txt', "a")

gameLoop = GameLoop(640, 480)

while gameLoop.isGameOn():
    gameLoop.mainLoop()

pygame.quit()
