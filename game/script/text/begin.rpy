label open:
    play music "bgm/日常的小曲.opus" fadein 1.0 volume 0.4
    scene sky with dissolve
    show luokun mohu with dissolve
    l mohu "如你所见"
    l mohu "这就是我"
    l mohu "罗坤"
    l mohu "一个帅到模糊的男人"
    l mohu "像我这么帅气的男人，开学会突然有一个一米六"
    l mohu "双马尾,看似高冷，外表却十分可爱"
    l mohu "带点傲娇小属性的同校小妹冲进我的教室"
    l mohu "用闪烁着泪花的眼睛和温柔细腻却带着一丝哭腔的声音"
    l mohu "深情的看着我并对我说"
    l mohu "我喜欢你很久了，为什么还是察觉不到我的心意呢"
    l mohu "不过是我的日常罢了"
    l mohu "毕竟"
    l mohu "如你所见"
    l mohu "这就是我"
    l mohu "罗坤"
    l mohu "一个帅到模糊的男人"
    return
#表白
label begin:
    play music "bgm/日常的小曲.opus" fadein 1.0 volume 0.4
    scene sky with rule_2
    n "星见学院一如既往樱花满天飘落"
    n "早川雪乃蹲在花坛边"
    n "目光却黏在不远处的路口"
    n "她的裙摆沾着几片樱花瓣"
    n "发梢别着一朵刚摘的白色雏菊"
    n "那是三年前罗坤帮她捡花苗时，落在他袖口的同款花"
    show zaochuan with dissolve
    z "（小声嘀咕）今天的樱花也开得好漂亮啊... 不知道罗坤桑会不会喜欢..."
    z "（突然挺直腰板，双手攥成拳头）不行不行！早川雪乃"
    z "今天可是你准备了三个月的‘告白日’"
    z "不能再像以前一样只敢偷偷看他了！"
    n "她从花坛旁的帆布包里掏出一张折得整齐的粉色信纸"
    n "展开看了眼，又迅速折好塞回口袋"
    n "指尖划过口袋边缘，三年前的记忆突然涌来"
    n "那天她摔在地上，指尖的血珠渗进泥土"
    n "是罗坤蹲下来用袖口擦去血迹"
    n "指尖碰到她皮肤时的温度，比初春的阳光还要暖"
    n "（眼眶微微发热）那时候罗坤桑明明那么温柔..."
    n "可为什么之后三年，他好像从来没注意过我呢？"
    scene street with rule_5
    show zaochuan with dissolve
    z "喜欢罗坤桑的一千零一天"
    z "三年来我每天都在这里守候"
    z "看着罗坤桑从对面走过"
    z "可他，从没有看过我一眼"
    hide zaochuan with dissolve
    show luokun zl1 with dissolve
    n "天空一声巨响,罗坤桑闪亮登场!!!"
    n "bang——bang——bangbang!"
    play sound "audio/sfx/bangbang.ogg"
    z xuanyun "天哪，难道今天就是我的幸运日吗"
    z shy "勇敢点，早川，把你的心声大声地喊出来吧"
    z shy "罗坤桑！我宣你"
    z shy "我的脑和我的心"
    z shy "我全身上下的每一个器官都在说着，我宣你！"
    l zl1"你喜欢谁？"
    z "罗 —— 坤 ——"
    l zl1"谁喜欢罗坤？"
    z shy "早 —— 川 —— 酱 ——"
    l zl1"我 —— 听 —— 不 —— 见！"
    n "一辆汽车飞驰而过创向了罗坤桑"
    play sound "audio/sfx/car.ogg" volume 3.0
    z sad "!!!"
    z sad "罗 —— 坤 —— 桑 ——"
    scene flower with dissolve
    n "粉色信纸从松开的指尖滑落，轻飘飘跌在沾染了樱花瓣的柏油路上"
    n "风卷着残樱掠过，信纸被吹得微微蜷缩，"
    n "边角蹭过地面的尘土，却依旧固执地露出折痕里未干的字迹。"
    n "樱花还在簌簌飘落，落在信纸上"
    n "遮住了 “喜欢你” 的尾字，又被风轻轻吹走。"
    n "信纸偶尔被风掀起一角，露出少女娟秀的笔迹，"
    n "转瞬又重重垂下，仿佛连纸张都在为这场戛然而止的告白叹息。"
    n "一场未完成的心事，渐渐被漫天樱雪掩埋。"
    $ renpy.movie_cutscene("video/begin.webm")
    n "由于经费原因,此处省略一个op"
    scene street with rule_3
    show luokun miss with dissolve
    l miss "（猛地侧身避开汽车，后背还沾着风的凉意，气息微急）"
    l miss  "小小汽车,颗秒！"
    play sound "audio/sfx/kemiao.ogg"
    l miss "（手擦过自己的头油，一个后撤步帅气转身，目光落在早川泛红的眼眶上)"
    l miss "好险... 早川同学，你刚才在喊我吗？"
    z shy "（眼神躲闪着不敢看他，手指死死绞着裙摆，声音细若蚊蚋）没、没有！我没喊你... 刚才是风吹得我认错人了！"
    l miss "（挑眉，目光落在她口袋露出的粉色信纸一角，嘴角带着一丝了然的笑意）是吗？可我好像听到有人说... 喜欢我？"
    z xuanyun "（瞳孔骤缩，像被踩中尾巴的兔子一样浑身绷紧）！！！"
    z xuanyun "（大脑一片空白，只剩下 “被听到了”“好丢脸”“怎么办” 的念头，眼泪都快急出来了）不、不是的！你听错了！"
    z shy "我、我还有事！先走了罗坤桑！"
    return

label sleep:
    scene sky with rule_1
    show luokun sleep1 at Transform(xalign=0.0, yalign=0.5) with dissolve
    wang "罗坤!罗坤!怎么还不起床"
    wang "拼好饭吃中毒了吗"
    wang "下水道的阴暗老鼠别yy了"
    wang "先起来把今天原神体力清了吧"
    stop music
    voice "voice/狗叫.ogg"
    n "罗坤睁开朦胧睡眼,伸了一个香香软软的小懒腰"
    voice "voice/掉毛.ogg"
    l sleep1 "王大爷,你掉毛吗"
    play music "bgm/大东北.ogg" fadein 1.0 volume 1.3
    show luokun sleep2 at Transform(xalign=0.5, yalign=1.0) with dissolve
    l sleep2 "又是新的一天,吾乃永劫修罗,你们的王回来了!"
    n "罗坤桑的侧颜一如既往的帅气，连刚睡醒的样子都很精神呢"
    l qishen "罗坤桑先是坐起身，揉了揉乱糟糟的头发"
    show luokun sleep3 at Transform(xalign=0.5, yalign=0.5) with dissolve
    l sleep3 "作为老op,起床第一件事当然是先把原神体力清了"
    voice "voice/原神启动.ogg"
    l sleep3 "原神启动"
    l sleep3 "啧，昨天睡前明明压好了发型，怎么还是有点翘...不过没关系,本王的颜值能hold住!"
    l sleep3 "昨天的原来是梦吗"
    l sleep3 "果然恋爱什么的是不会降临到我的头上的吧"
    l sleep4 "算了算了再睡会"
    l sleep4 "这次我要梦一个36D大雷黑长直"
    l sleep1 "zzz"
    l sleep1 "zzz"
return