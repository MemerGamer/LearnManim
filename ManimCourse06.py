from manim import *


# 6.)
class Updaters(Scene):
    def construct(self):
        num = MathTex("ln(2)")
        box = always_redraw(
            lambda: SurroundingRectangle(
                num, color=BLUE, fill_opacity=0.4, fill_color=RED, buff=2
            )
        )

        name = always_redraw(lambda: Tex("Hunor").next_to(box, DOWN, buff=0.25))
        self.play(Create(VGroup(num, box, name)))
        self.play(num.animate.shift(RIGHT * 2), run_time=2)
        self.wait()
