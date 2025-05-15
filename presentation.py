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

        text_passing_screening_CV = Text("Passing screening (CV)", font_size=40)
        text_passing_screening_CV.move_to(text_how_to_faang.get_bottom()).shift(DOWN)
        self.play(
            Write(text_passing_screening_CV),
        )

        self.next_slide()

        text_safeish_route = Text("Safe(ish?) route", font_size=36)
        text_safeish_route.move_to(text_passing_screening_CV.get_bottom()).shift(DOWN * 2 + LEFT * 4)
        self.play(Write(text_safeish_route))
        self.wait(0.5)

        bullet_list_safe_route = BulletedList(
            "Local internships",
            "Contests/Hackathons (and winning)",
            "Previous jobs",
            buff=MED_LARGE_BUFF,
            font_size=32,
        )
        bullet_list_safe_route.move_to(text_safeish_route.get_bottom()).shift(DOWN * 2 + RIGHT*1.5)
        self.play(Write(bullet_list_safe_route))

        self.next_slide()

        text_red_pilled_route = Text("Riskier Red Pilled route", font_size=40)
        text_red_pilled_route.move_to(text_passing_screening_CV.get_bottom()).shift(DOWN * 2 + RIGHT * 4)
        self.play(Write(text_red_pilled_route))
        self.wait(0.5)

        bullet_list_risker_route = BulletedList(
            "Startups",
            "Open-source",
            "Research",
            buff=MED_LARGE_BUFF,
            font_size=32,
        )

        bullet_list_risker_route.move_to(text_red_pilled_route.get_bottom()).shift(DOWN * 2)
        self.play(Write(bullet_list_risker_route))

        self.next_slide()

        self.play(
            AnimationGroup(
                FadeOut(text_passing_screening_CV),
                FadeOut(text_safeish_route),
                FadeOut(text_red_pilled_route),
                FadeOut(bullet_list_safe_route),
                FadeOut(bullet_list_risker_route),
                lag_ratio=0.125
            )
        )

        text_eugen = Text("Eugen", font_size=32)
        text_eugen_cv = Text("2 (failed) startups, olympiads hs+ACM, visualization/simulation projects", font_size=24)
        text_eugen.to_edge(LEFT).shift(UP*2)
        text_eugen_cv.next_to(text_eugen, RIGHT, aligned_edge=LEFT).shift(RIGHT)

        text_antonio = Text("Antonio", font_size=32)
        text_antonio_cv = Text("Internship (bosch), olympiads hs, AI+embedded projects", font_size=24)
        text_antonio.to_edge(LEFT).shift(UP)
        text_antonio_cv.next_to(text_antonio, RIGHT, aligned_edge=LEFT).shift(RIGHT)

        text_mihoc = Text("Mihoc", font_size=32)
        text_mihoc_cv = Text("Internship+job linnify 2YOE, volunteering", font_size=24)
        text_mihoc.to_edge(LEFT)
        text_mihoc_cv.next_to(text_mihoc, RIGHT, aligned_edge=LEFT).shift(RIGHT)

        text_octavian = Text("Octavian", font_size=32)
        text_octavian_cv = Text("Internship (bitdefender), olympiads hs+ACM, small projects", font_size=24)
        text_octavian.to_edge(LEFT).shift(-UP)
        text_octavian_cv.next_to(text_octavian, RIGHT, aligned_edge=LEFT).shift(RIGHT)

        text_tudor = Text("Tudor", font_size=32)
        text_tudor_cv = Text("3 Internships, part-time NTT 8M, olympiads hs+ACM", font_size=24)
        text_tudor.to_edge(LEFT).shift(-2*UP)
        text_tudor_cv.next_to(text_tudor, RIGHT, aligned_edge=LEFT).shift(RIGHT)

        text_alex = Text("Alex", font_size=32)
        text_alex_cv = Text("2 (failed) startups (one with robotics), hackathons, web scraping", font_size=24)
        text_alex.to_edge(LEFT).shift(-3*UP)
        text_alex_cv.next_to(text_alex, RIGHT, aligned_edge=LEFT).shift(RIGHT)

        self.play(
            AnimationGroup(
                Write(text_eugen),
                Write(text_eugen_cv),

                Write(text_antonio),
                Write(text_antonio_cv),

                Write(text_mihoc),
                Write(text_mihoc_cv),

                Write(text_octavian),
                Write(text_octavian_cv),

                Write(text_tudor),
                Write(text_tudor_cv),

                Write(text_alex),
                Write(text_alex_cv),

                lag_ratio=0.125
            )
        )

        self.next_slide()

        self.play(
            AnimationGroup(
                FadeOut(text_eugen),
                FadeOut(text_eugen_cv),

                FadeOut(text_antonio),
                FadeOut(text_antonio_cv),

                FadeOut(text_mihoc),
                FadeOut(text_mihoc_cv),

                FadeOut(text_octavian),
                FadeOut(text_octavian_cv),

                FadeOut(text_tudor),
                FadeOut(text_tudor_cv),

                FadeOut(text_alex),
                FadeOut(text_alex_cv),
                lag_ratio=0.05
            )
        )

        timeline = NumberLine(
            x_range=[0,10,1],
            length=10,
            include_numbers=True,
            include_ticks=True,
        ).scale(0.8)
        text_planning_timeline = Text("Planning timeline", font_size=48)
        text_planning_timeline.move_to(text_how_to_faang.get_center())

        self.play(
            Create(timeline),
            ReplacementTransform(text_how_to_faang, text_planning_timeline)
        )

        self.next_slide()

        start_point = timeline.number_to_point(0)
        end_point3 = timeline.number_to_point(3)
        end_point6 = timeline.number_to_point(6)
        line3m = Line(start=start_point, end=end_point3)
        line6m = Line(start=start_point, end=end_point6)
        text_neetcode150 = Text("Neetcode (150), 3pb/d", font_size=36)
        text_leetcode = Text("Neetcode 150 + 200pb", font_size=36)

        section_brance3m = Brace(
            line3m,
            direction=DOWN,
            buff=MED_LARGE_BUFF,
            color=YELLOW,
        )
        text_neetcode150.move_to(section_brance3m.get_bottom()).shift(DOWN)

        self.play(
            GrowFromCenter(section_brance3m),
            Write(text_neetcode150)
        )

        section_brace6m = Brace(
            line6m,
            direction=UP,
            buff=MED_LARGE_BUFF,
            color=YELLOW,
        )
        text_leetcode.move_to(section_brace6m.get_top()).shift(UP)

        self.play(
            GrowFromCenter(section_brace6m),
            Write(text_leetcode)
        )

        self.next_slide()

        extended_timeline = NumberLine(
            x_range=[0,24, 1],
            length=24,
            include_numbers=True,
            include_ticks=True,
        )
        self.play(
            ReplacementTransform(timeline, extended_timeline),
            FadeOut(section_brace6m),
            FadeOut(section_brance3m),
            FadeOut(text_leetcode),
            FadeOut(text_neetcode150)
        )

        self.play(
            extended_timeline.animate.scale(0.5),
        )

        start_point = extended_timeline.number_to_point(0)
        end_point4 = extended_timeline.number_to_point(4)
        end_point10 = extended_timeline.number_to_point(10)
        end_point24 = extended_timeline.number_to_point(24)

        line4m = Line(start=start_point, end=end_point4)
        line10m = Line(start=end_point4, end=end_point10)
        line24m = Line(start=start_point, end=end_point24)

        bracket4m = Brace(
            line4m,
            direction=DOWN,
            buff=SMALL_BUFF,
        ).shift(DOWN/2)

        bracket10m = Brace(
            line10m,
            direction=DOWN,
            buff=SMALL_BUFF,
        ).shift(DOWN/2)
        bracket24m = Brace(
            line24m,
            direction=UP,
            buff=SMALL_BUFF,
        ).shift(UP/2)


        text_leetcode = Text("300 leetcode", font_size=24)
        text_project = Text("CV project bomb", font_size=24)
        text_apply_and_interview = Text("Apply and interview", font_size=24)
        text_leetcode.move_to(bracket4m.get_bottom()).shift(DOWN)
        text_project.move_to(bracket10m.get_bottom()).shift(DOWN)
        text_apply_and_interview.move_to(bracket24m.get_top()).shift(UP)

        self.play(
            AnimationGroup(
                GrowFromCenter(bracket4m),
                GrowFromCenter(bracket10m),
                GrowFromCenter(bracket24m),
                Write(text_leetcode),
                Write(text_project),
                Write(text_apply_and_interview),
                lag_ratio=0.4
            )
        )

        self.next_slide()

        self.play(
            AnimationGroup(
                FadeOut(bracket4m),
                FadeOut(bracket10m),
                FadeOut(bracket24m),
                FadeOut(text_leetcode),
                FadeOut(text_project),
                FadeOut(text_apply_and_interview),
                lag_ratio=0.125
            )
        )

        extended_timeline_numberless = NumberLine(
            x_range=[0,24, 1],
            length=24,
            include_numbers=False,
            include_ticks=True,
        )

        self.play(
            ReplacementTransform(extended_timeline, extended_timeline_numberless),
        )

        extended_timeline_point6 = extended_timeline_numberless.number_to_point(6)
        dot_may = Dot(extended_timeline_point6, radius=0.1, color=YELLOW)
        line_may = Line(start=extended_timeline_point6, end=extended_timeline_point6 + DOWN*1.5).shift(DOWN/2)
        text_may = Text("May (now)", font_size=24)
        text_may.move_to(line_may.get_bottom()).shift(DOWN/2)

        self.play(
            AnimationGroup(
                GrowFromCenter(dot_may),
                Create(line_may),
                Write(text_may)
            )
        )

        self.next_slide()

        extended_timeline_point13 = extended_timeline_numberless.number_to_point(13)
        dot_sept = Dot(extended_timeline_point13, radius=0.1, color=YELLOW)
        line_sept = Line(start=extended_timeline_point13, end=extended_timeline_point13 + DOWN*1.5).shift(DOWN/2)
        text_sept = Text("Sept", font_size=24)
        text_sept.move_to(line_sept.get_bottom()).shift(DOWN/2)

        extended_timeline_point15 = extended_timeline_numberless.number_to_point(15)
        dot_nov = Dot(extended_timeline_point15, radius=0.1, color=YELLOW)
        line_nov = Line(start=extended_timeline_point15, end=extended_timeline_point15 + DOWN*1.5).shift(DOWN/2)
        text_nov = Text("Nov", font_size=24)
        text_nov.move_to(line_nov.get_bottom()).shift(DOWN/2)

        self.play(
            AnimationGroup(
                GrowFromCenter(dot_sept),
                Create(line_sept),
                Write(text_sept),

                GrowFromCenter(dot_nov),
                Create(line_nov),
                Write(text_nov)
            )
        )

        line_app = Line(extended_timeline_point13, extended_timeline_point15)
        bracket_app = Brace(
            line_app,
            direction=UP,
            buff=SMALL_BUFF,
        ).shift(UP/2)
        text_app = Text("Applications", font_size=24)
        text_app.move_to(bracket_app.get_top()).shift(UP/2)

        self.play(
            GrowFromCenter(bracket_app),
            Write(text_app)
        )

        self.next_slide()

        vgroupall = VGroup(extended_timeline_numberless, dot_may, dot_sept, dot_nov, bracket_app, text_app, text_planning_timeline, line_nov, line_may, line_sept, text_nov, text_may, text_sept)
        text_othernots_qa = Text("Other notes + QA", font_size=48)

        self.play(
            ReplacementTransform(vgroupall, text_othernots_qa)
        )











