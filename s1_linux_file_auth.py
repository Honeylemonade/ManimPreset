from commonElm.text import *


class S1(Scene):
    """
    介绍整体视频内容结构
    """

    def construct(self):
        # 开头
        # grid = NumberPlane()
        # self.add(grid)
        t = hText("Linux用户、用户组与文件权限")
        self.play(FadeIn(t))
        self.play(t.animate.scale(1.5).to_edge(UP * 3))
        self.wait()
        # 介绍视频内容
        st1 = hText("1.介绍权限的由来")
        st2 = hText("2.介绍用户与用户组").next_to(st1, DOWN).align_to(st1, LEFT)
        st3 = hText("3.介绍文件的rwx权限").next_to(st2, DOWN).align_to(st1, LEFT)
        st4 = hText("4.实际操作如何修改权限").next_to(st3, DOWN).align_to(st1, LEFT)
        g = VGroup(st1, st2, st3, st4)
        for st in g:
            self.play(Write(st))


class S2(Scene):
    """
    介绍权限的由来
    """

    def construct(self):
        # grid = NumberPlane()
        # grid.add_coordinates()
        # self.add(grid)

        # 介绍视频内容
        t = hText("Linux为什么出现了权限？")
        self.play(
            FadeIn(t).mobject.animate.scale(1.5).move_to(UP * 3,
                                                         aligned_edge=UP))

        p1 = Paragraph('我们知道，在过去', "计算资源是非常昂贵的",
                       color=BLACK).scale(0.7).move_to(LEFT * 6 + UP,
                                                       aligned_edge=UL)

        server_img = ImageMobject("resource/s1/服务器.png").scale(0.5)
        money_img = ImageMobject("resource/s1/钱币.png").scale(0.3).move_to(
            RIGHT * 5)
        user_img = ImageMobject("resource/s1/用户.png").scale(0.3).move_to(
            RIGHT * 3 + DOWN * 3)

        animations1 = [
            FadeIn(server_img).mobject.animate.move_to(RIGHT * 3),
            Write(p1)
        ]

        self.play(AnimationGroup(*animations1, lag_ratio=0))
        self.play(FadeIn(money_img))
        p2 = Paragraph('因此为了保证资源被充分利用',
                       color=BLACK).scale(0.7).move_to(LEFT * 6,
                                                       aligned_edge=UL)
        self.play(Write(p2))

        p3 = Paragraph("电脑上就出现了多用户的概念。", "即一台电脑可以被多个用户使用",
                       color=BLACK).scale(0.7).move_to(LEFT * 6 + DOWN * 0.5,
                                                       aligned_edge=UL)

        ani2 = [Write(p3), FadeIn(user_img)]
        self.play(AnimationGroup(*ani2, lag_ratio=0))

        users = []
        for i in range(5):
            cp_u = user_img.copy()
            cp_u.shift(LEFT * (i - 2))
            users.append(cp_u)

        self.play(AnimationGroup(FadeIn(Group(*users)), FadeOut(user_img)))

        # 箭头指向
        arrows: list[ImageMobject] = []
        for usr in users:
            usr: ImageMobject
            arrows.append(
                Arrow(start=usr.get_top(),
                      end=server_img.get_bottom(),
                      color=GOLD,
                      stroke_width=3,
                      max_tip_length_to_length_ratio=0.05))

        self.play(Create(VGroup(*arrows)))

        # 上传秘密
        secret_img = ImageMobject("resource/s1/秘密.png").scale(0.4).move_to(
            RIGHT * 1 + DOWN * 2)
        self.play(
            FadeIn(secret_img).mobject.animate.move_to(
                server_img.get_center()))

        # 其他用户拿到秘密
        arrows2: list[ImageMobject] = []
        for usr in users:
            usr: ImageMobject
            arrows2.append(
                Arrow(start=secret_img.get_center(),
                      end=usr.get_top(),
                      color=RED,
                      stroke_width=3,
                      max_tip_length_to_length_ratio=0.05))
        self.play(Create(VGroup(*arrows2)))
