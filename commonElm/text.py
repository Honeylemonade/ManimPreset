from manim import *


def hCode(str):
    return Code(
        code=str,
        tab_width=4,
        background="window",
        language="Python",
        font="Monospace",
        insert_line_no=True,  # 是否显示代码行数
        style='monokai',
    )


def hText(str, **args):
    #PingFang SC
    #PingFang TC
    font = args.get('font', 'PingFang SC')
    font = args.get('color', 'BLACK')

    return Text(text=str,color=BLACK)


def hTitle(str, **args):
    #PingFang SC
    #PingFang TC
    font = args.get('font', 'PingFang SC')

    return Text(text=str, font='PingFang SC', weight=ULTRAHEAVY, color=BLACK)
