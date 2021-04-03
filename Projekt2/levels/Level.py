from abc import abstractmethod


class Level:
    def __init__(self, screen):
        self.isActive = True
        self.gameIsPaused = False
        self.screen = screen
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

    @abstractmethod
    def handleInput(self, key):
        return

    @abstractmethod
    def nextLoop(self):
        return

    def deactivateLevel(self):
        self.isActive = False

    def togglePause(self):
        self.gameIsPaused = not self.gameIsPaused
