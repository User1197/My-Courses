from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.uix.image import Image

BACKGROUND_IMAGE = "C:/Users/wcai/Desktop/5 Personal Projects/My Courses/Kivy/Example Projects/r1chardj0n3s-kivy-game-tutorial-a8275f381cd7/flappy/images/background.png"
BIRD_IMAGE = "C:/Users/wcai/Desktop/5 Personal Projects/My Courses/Kivy/Example Projects/r1chardj0n3s-kivy-game-tutorial-a8275f381cd7/flappy/images/bird.png"

class Sprite(Image):
    def __init__(self, **kwargs):
        super(Sprite, self).__init__(**kwargs)
        self.size = self.texture_size

class Background(Widget):
    def __init__(self, source):
        super(Background, self).__init__()
        self.image = Sprite(source=source)
        self.add_widget(self.image)
        self.size = self.image.size
        self.image_dupe = Sprite(source=source, x=self.width)
        self.add_widget(self.image_dupe)

    def update(self):
        self.image.x -= 2
        self.image_dupe.x -= 2

        if self.image.right <= 0:
            self.image.x = 0
            self.image_dupe.x = self.width

class Game(Widget):
    def __init__(self):
        super(Game, self).__init__()
        self.background = Background(source=BACKGROUND_IMAGE)
        self.size = self.background.size
        self.add_widget(self.background)
        Clock.schedule_interval(self.update, 10/60.0)

    def update(self, *ignore):
        self.background.update()

class GameApp(App):
    def build(self):
        #return Game()
        game = Game()
        Window.size = game.size
        return game

if __name__ == "__main__":
    GameApp().run()
