# 游戏的脚本可置于此文件中。
# script.rpy
image black:
    "#000000"
label splashscreen:
    scene black
    show warning:
        xsize 1950
        ysize 1100
    with dissolve
    pause 2.0
    hide warning with fade
 
    show title:
        xsize 1950
        ysize 1100
    with dissolve
    play sound "audio/sfx/title.ogg"
    pause 2.0
    hide title with fade

    return


# 游戏在此开始。


label start:
    call open from _call_open
    call begin from _call_begin           
    call sleep from _call_sleep
    call one from _call_one
    call classroom from _call_classroom
    call two from _call_two
    call restaurant from _call_restaurant
    call three from _call_three
    call show_credits from _call_show_credits

    # 此处显示各行对话。
    

    # 此处为游戏结尾。

    return
