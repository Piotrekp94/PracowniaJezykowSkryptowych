from abc import abstractmethod


class Level:
    def __init__(self, screen, player):
        self.isActive = True
        self.gameIsPaused = False
        self.screen = screen
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.player = player

    @abstractmethod
    def handleInput(self, key):
        return

    @abstractmethod
    def nextLoop(self):
        return

    @abstractmethod
    def draw(self):
        return

    def deactivateLevel(self):
        self.isActive = False

    def togglePause(self):
        self.gameIsPaused = not self.gameIsPaused
