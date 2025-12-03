label open_movie_playing:
    $ skipping_co = _skipping
    $ dismiss_pause_co = _dismiss_pause
    $ game_menu_screen_co = _game_menu_screen
    $ rollback_co = _rollback
    
    # 禁用输入
    $ _skipping = False
    $ _dismiss_pause = False
    $ _game_menu_screen = None
    $ _rollback = False
    $ config.allow_skipping = False

    show screen block_mouse_input
    # 播放视频
    # play movie "video/nima.webm" noloop
    $ renpy.movie_cutscene("video/nima.webm")
    hide screen block_mouse_input
    # 恢复输入设置
    $ _skipping = skipping_co
    $ _dismiss_pause = dismiss_pause_co
    $ _game_menu_screen = game_menu_screen_co
    $ _rollback = rollback_co

    return

screen block_mouse_input():
    # 将该屏幕设置为模态，这意味着它下方的其他屏幕和按钮将无法接收输入
    modal True

    frame:
        area (0, 0, 1.0, 1.0) 
        button action NullAction()