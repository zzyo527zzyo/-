define rule_1 = ImageDissolve("images/rule/rule_1.png",1.5,ramplen=8)
define rule_2 = ImageDissolve("images/rule/rule_2.png",1.5,ramplen=8)
define rule_3 = ImageDissolve("images/rule/rule_3.png",1.5,ramplen=8)
define rule_4 = ImageDissolve("images/rule/rule_4.png",1.5,ramplen=8)
define rule_5 = ImageDissolve("images/rule/rule_5.png",1.5,ramplen=8)
define rule_6 = ImageDissolve("images/rule/rule_6.png",1.5,ramplen=8)
define rule_7 = ImageDissolve("images/rule/rule_7.png",1.5,ramplen=8)
define rule_8 = ImageDissolve("images/rule/rule_8.png",1.5,ramplen=8)
define rule_9 = ImageDissolve("images/rule/rule_9.png",1.5,ramplen=8)
define rule_10 = ImageDissolve("images/rule/rule_10.png",1.5,ramplen=8)
define rule_11 = ImageDissolve("images/rule/rule_11.png",1.5,ramplen=8)
define rule_12 = ImageDissolve("images/rule/rule_12.png",1.5,ramplen=8)
define rule_13 = ImageDissolve("images/rule/rule_13.png",1.5,ramplen=8)


init python:
    transition_mytype_1 = ComposeTransition(
        Fade(1,0.2,1),                
        before=moveoutleft,      
        after=moveinright                    
    )
    
    transition2 = ComposeTransition(
        Dissolve(2.0),           
        before=Fade(0.5, 0, 0),  
        after=Fade(0, 0, 1.0)    
    )