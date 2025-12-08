from manim import *

class ShowSVG(Scene):
    def construct(self):
        # Load your SVG file (must be in the same folder)
        svg = SVGMobject("test.svg")
        svg.scale(2)            # Make it bigger if needed
        svg.move_to(ORIGIN)     # Center it on the screen
        self.play(FadeIn(svg))  # Fade it in
        self.wait(2)            # Hold on screen for 2 seconds
