from manim import *


# 3.)
class Errors(Scene):
    def construct(self):
        c = Circle(radius=2)
        self.play(Write(c))
