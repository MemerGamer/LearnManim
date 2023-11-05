from manim import *


# 9.)
class UpdatedGraphing(Scene):
    def construct(self):
        k = ValueTracker(-4)
        ax = (
            Axes(x_range=[-4, 4, 1], y_range=[-2, 16, 2], x_length=10, y_length=6)
            .to_edge(DOWN)
            .add_coordinates()
        ).set_color(WHITE)

        func = ax.plot(lambda x: x**2, x_range=[-4, 4], color=BLUE)

        slope = always_redraw(
            lambda: ax.get_secant_slope_group(
                x=k.get_value(),
                graph=func,
                dx=0.01,
                secant_line_color=GREEN,
                secant_line_length=3,
            )
        )

        pt = always_redraw(
            lambda: Dot().move_to(
                ax.c2p(k.get_value(), func.underlying_function(k.get_value()))
            )
        )

        self.add(ax, func, slope, pt)
        self.wait()
        self.play(k.animate.set_value(4), run_time=3)
