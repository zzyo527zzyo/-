label z:
    scene street with rule_2
    play music "bgm/难过.opus"
    show zaochuan with dissolve 
    n "清晨的樱花道还没什么人"
    n "粉色花瓣沾着露水"
    n "在石板路上铺了薄薄一层。"
    n "罗坤躲在最大的那棵樱花树后，探头探脑地望着路口。"
    l "这次一定要堵到她,问清楚上次的粉色信是怎么回事"
    n "远处传来轻快的脚步声，早川雪乃背着帆布包，哼着歌从路口出现。"
    n "罗坤深吸一口气，猛地从树后跳出来。"
    l "你好呀美丽的小姐"
    z xuanyun "（吓了一跳，水壶差点脱手）呀！罗、罗坤桑？！"
    z xuanyun "你怎么会在这里...还躲在树后面..."
    l "我在等你啊"
    l "说吧，上次在樱花道上是不是想跟我说些什么"
    z shy "（瞬间脸红到耳根，慌忙摆手）没、没想说什么啊！"
    n "早川说着就要绕开罗坤，却被他一把拉住手腕"
    n "樱花花瓣落在两人交握的手上。"
    l "你是不是...喜欢我？"
    z sad "（猛地低下头，眼泪啪嗒掉在水壶上）呜...被发现了..."
    z sad "我、我本来想等其他机会说的..."
    n "早川深吸一口气，突然停下脚步，转身面对着罗坤，双手将攥了很久的信封递过去。"
    z shy "罗坤桑！这个给你！"
    l "（接过信封）这是..."
    z shy"明明自己知道还问"
    z sad"我喜欢罗坤桑！从三年前你帮我捡花苗的时候就喜欢了！"
    n "早川的声音带着哭腔，眼泪在眼眶里打转，却倔强地仰着头看着罗坤。"
    z sad "我知道我可能有点笨，也不像雾岛同学那么可爱，更不像绯月小姐那么温柔..."
    z sad "但我会努力变得更好的！罗坤桑...你愿意和我交往吗？"
    l "（愣住，手里的信封变得滚烫）雪乃同学..."
    n "粉色的樱花瓣落在两人之间，空气仿佛凝固了，只有早川带着期待与不安的呼吸声。"
    z "（小声）罗坤桑...你不用马上回答我的..."
    z "只要...只要你能明白我的心意就好..."
    stop music
    menu:
        "接收早川雪乃的告白":
            jump CGz
        "拒绝早川雪乃的告白":
            jump reject_z
    return

label CGz:
    play music "bgm/难过.opus"
    scene cg
    n "特殊CGplaying"
    $ achievement.grant("特殊CG好看吗")
    $ renpy.notify("成就解锁:特殊CG好看吗")
    n "特殊CGplaying"
    n "特殊CGplaying"
 
    return

label reject_z:
    play music "bgm/难过.opus"
    scene street with rule_3
    show luokun jy with dissolve  
    l jy"你为啥跟我直接表白啊?"
    l jy"嘎啦game里不是这样!"
    l jy"你应该多跟我聊天"
    l jy"然后提升我的好感度"
    $ achievement.grant("嘎啦game糕手")
    $ renpy.notify("成就解锁:嘎啦game糕手")
    l jy"偶尔给我送送礼物"
    l zl2"然后在那个特殊节日时候跟我有特殊互动"
    l zl2"最后在某个我内心神秘事件中"
    l zl2"向我表白，我同意跟你在一起"
    l zl2"然后我给你看我的特殊CG啊"
    l zl2"你怎么直接上来跟我表白!"
    l zl2"嘎啦game里根本不是这样!"
    l zl2"我不接受!"
    
return
 
label haiwang:
    play music "bgm/难过.opus"
    scene sun with rule_1
    w "臭杂鱼你还想当海王"
    $ achievement.grant("我靠袁华")
    $ renpy.notify("成就解锁:我靠袁华")
    w "喜欢跟很多人搞暧昧是吧"
    l "什么叫我跟很多人搞暧昧啊"
    l "嘎啦game里就是这样"
    l "我单身,你也单身,他们都是单身"
    l "她们都是可攻略角色"
    l "我当然可以和她们聊天啊"
    l "那如果最后每一个人我都聊失败了"
    l "这不是更可怜吗"
    l "在说了我连你对我的好感度有多少我都不知道"
    l "我都还没开始玩你这条支线"
    l "你先排队吧好不好"
    l "什么叫只可以更你聊天啊"
    l "你这个人怎么可以这么自私"
    l "我不跟你聊啦"
    return