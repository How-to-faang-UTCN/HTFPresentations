from manim import *
from manim_slides import Slide

class Presentation(Slide):
    def construct(self):
        title_text = Text("How to FAANG", font_size=48)

        title_circle = Circle(radius=1, color=BLUE)
        title_circle.surround(title_text, buffer_factor=1.5)

        dot_radius = 0.1
        dot_initial_position = title_circle.get_right()
        moving_dot = Dot(point=dot_initial_position, radius=dot_radius, color=RED_D)

        self.play(
            Write(title_text),
            Create(title_circle),
            run_time=2
        )

        angle_tracker = ValueTracker(0)
        def update_dot_position(mob):
            angle = angle_tracker.get_value()
            new_pos = title_circle.point_at_angle(angle)
            mob.move_to(new_pos)
        moving_dot.add_updater(update_dot_position)

        self.play(FadeIn(moving_dot))
        self.next_slide(loop=True)
        self.play(
            angle_tracker.animate.set_value(2 * PI),
            run_time=5,
            rate_func=linear
        )
        self.next_slide()

        self.play(
            FadeOut(moving_dot),
            FadeOut(title_circle),
        )

        title_story_part = Text("The story of origins", font_size=48)
        title_story_part.to_edge(UP)
        self.play(ReplacementTransform(title_text, title_story_part))

        self.next_slide()
        # rejections1 = ImageMobject("rejections1.png")
        # rejections2 = ImageMobject("rejections2.png")


