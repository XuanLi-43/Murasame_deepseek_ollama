#加载音频
define m1 = "/audio/bgm/Angel Note,井ノ原智 - キズナヒトツ Instrument Version.ogg"
define m2 = "/audio/bgm/Angel Note,井ノ原智 - くつろぎの間.ogg"
define m3 = "/Angel Note,井ノ原智 - 輝きの瞬間.ogg"
define m4 = "/audio/bgm/Angel Note,井ノ原智 - 身も心も….ogg"
define m5 = "/audio/bgm/Angel Note,井ノ原智 - 神様の祝福.ogg"
define m6 = "/audio/bgm/Angel Note,井ノ原智 - 縁結び.ogg"


#加载live2d模型
define config.gl2 = True
define _live2d_fade = True  
image bg = r"/images/background.png"
image Murasame = Live2D(r"live2d/live2dmodel/Murasame.model3.json",\
scale=.6,loop=True, seamless=True,\
aliases={"No_movement" : "motion01", "speak1" : "motion02", "speak2" : "motion03", "speak3" : "motion04", "speak4" : "motion07" , "speak5" : "motion11"}) 

#live2d随机动作
init python:
    def RandomMurasameMotion_func():
        import random
        motion_list = ["motion02", "motion03", "motion04"]
        murasame_motion = renpy.random.choice(motion_list)
        return murasame_motion



#定义flag值，用于判断是否执行默认设定
define DeepseeekDefault_flag = False
define OllamaDefault_flag = False


init python:
    # 禁用回退功能
    config.rollback_enabled = False

    # 禁用自动保存
    config.has_autosave = False

    # 禁用快速存档
    config.quicksave_slots = 0

