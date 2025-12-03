# 定义制作人员信息
# 最简单的滚动制作人员信息
label show_credits:
    # 隐藏其他界面
    scene black
    
    # 显示滚动制作人员
    show expression Text(_("""
罗坤桑の恋爱物语

制作人员


动作指导：
    罗坤
剧本：
    卑微王二狗
程序：
    卑微王二狗
美术：
    sora
配音：
    暂无

特别感谢
所有玩家

谢谢游玩！
"""), size=36, color="#fff", xalign=0.5) as credits:
        yalign 1.0  # 从屏幕底部开始
        linear 10.0 yalign 0.0  # 20秒内滚动到顶部
    
    # 显示跳过按钮
    screen skip_credits:
        textbutton "跳过" action Jump("skip_credits") align (0.95, 0.05)
    
    show screen skip_credits
    $ renpy.pause(10.0, hard=True)
    hide screen skip_credits
    
    label skip_credits:
    hide credits
    return