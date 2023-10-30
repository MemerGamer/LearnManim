from manim import *


# 4.)
class Library(Scene):
    def construct(self):
        ax = Axes()

        self.play(Create(ax))
