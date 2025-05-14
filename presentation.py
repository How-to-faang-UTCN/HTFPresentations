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
        rejections1 = ImageMobject("rejections1.png").scale(0.2)
        rejections2 = ImageMobject("rejections1.png").scale(0.2)
        rejections1.shift(LEFT*3).rotate(PI/16)
        rejections2.shift(RIGHT*3).rotate(-PI/16)

        rejections1_text = Text("38 Rejections, 1 offer", font_size=30)
        rejections1_text.move_to(rejections1.get_bottom())
        rejections1_text.shift(1 * DOWN)

        rejections2_text = Text("124 Rejections, 1 offer", font_size=30)
        rejections2_text.move_to(rejections2.get_bottom())
        rejections2_text.shift(1 * DOWN)

        self.play(
            AnimationGroup(
                FadeIn(rejections1, run_time=0.5),
                FadeIn(rejections2, run_time=0.5),
                Write(rejections1_text),
                Write(rejections2_text),
                lag_ratio=0.5
            )
        )

        self.next_slide()

        text_how_to_not_faang = Text("How to not FAANG", font_size=48)
        text_how_to_not_faang.move_to(title_story_part.get_center())

        self.play(
            AnimationGroup(
                FadeOut(rejections1),
                FadeOut(rejections2),
                FadeOut(rejections1_text),
                FadeOut(rejections2_text),
            )
        )
        self.wait(1)
        self.play(
            ReplacementTransform(title_story_part, text_how_to_not_faang),
        )

        self.next_slide()
        bullet_list_how_to_not_faang = BulletedList(
            "Take tests at 6AM in the morning",
            "Put your interviews as late as possible",
            "Miss all the deadlines",
            buff=MED_LARGE_BUFF,
            font_size=32,
        )
        self.play(
            Write(bullet_list_how_to_not_faang),
        )
        self.next_slide()
        self.play(
            FadeOut(bullet_list_how_to_not_faang),
        )
        self.next_slide()

        # SECOND PART OF THE PRESENTATION INTRO + DESCRIPTION

        text_how_to_faang = Text("How to FAANG!", font_size=48)
        text_how_to_faang.shift(UP)
        self.play(ReplacementTransform(text_how_to_not_faang, text_how_to_faang))

        self.next_slide()
        tate_image = ImageMobject("tate.jpg").scale(1).set_opacity(0.075)
        self.play(
            FadeIn(tate_image, run_time=10),
        )
        self.play(
            FadeOut(tate_image, run_time=2),
        )

        self.next_slide()
        title_money = Text("Money (east)", font_size=40)
        title_money.move_to(text_how_to_faang.get_center())
        title_money_value_intern = Text("1500-2000$ at internship", font_size=24)
        title_money_value_manager = Text("6000+$ at senior+", font_size=24)

        self.play(
            FadeIn(title_money),
            title_money.animate.shift(4*LEFT + 2*DOWN)
        )
        self.wait(0.5)
        title_money_value_intern.move_to(title_money.get_bottom()).shift(DOWN)
        self.play(Write(title_money_value_intern))
        self.wait(0.5)
        title_money_value_manager.move_to(title_money_value_intern.get_bottom()).shift(DOWN)
        self.play(Write(title_money_value_manager))

        self.next_slide()

        text_prestige = Text("Prestige", font_size=40)
        text_prestige.move_to(text_how_to_faang.get_center())
        text_startups = Text("Positioning for startups", font_size=24)
        text_guaranteed_jobs = Text("(Mostly) Guaranteed jobs", font_size=24)

        self.play(
            FadeIn(text_prestige),
            text_prestige.animate.shift(2*DOWN)
        )
        self.wait(0.5)
        text_startups.move_to(text_prestige.get_bottom()).shift(DOWN)
        self.play(Write(text_startups))
        self.wait(0.5)
        text_guaranteed_jobs.move_to(text_startups.get_bottom()).shift(DOWN)
        self.play(Write(text_guaranteed_jobs))

        self.next_slide()

        text_knowledge = Text("Knowledge", font_size=40)
        text_knowledge.move_to(text_how_to_faang.get_center())
        text_unique_systems = Text("Unique systems", font_size=24)
        text_smart_people = Text("Smart people", font_size=24)

        self.play(
            FadeIn(text_knowledge),
            text_knowledge.animate.shift(2*DOWN + 4 * RIGHT)
        )
        self.wait(0.5)
        text_unique_systems.move_to(text_knowledge.get_bottom()).shift(DOWN)
        self.play(Write(text_unique_systems))
        self.wait(0.5)
        text_smart_people.move_to(text_unique_systems.get_bottom()).shift(DOWN)
        self.play(Write(text_smart_people))

        self.next_slide()

        self.play(
            text_how_to_faang.animate.to_edge(UP),
        )

        self.play(
            AnimationGroup(
                FadeOut(title_money),
                FadeOut(title_money_value_intern),
                FadeOut(title_money_value_manager),

                FadeOut(text_prestige),
                FadeOut(text_startups),
                FadeOut(text_guaranteed_jobs),

                FadeOut(text_knowledge),
                FadeOut(text_unique_systems),
                FadeOut(text_smart_people),
                lag_ratio=0.125
            )
        )





