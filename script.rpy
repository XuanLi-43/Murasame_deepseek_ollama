label start:
    $ deepseek_conversation_history.clear()
    $ ollama_conversation_history.clear()

    scene bg
    menu ChoiceModelInfo_menu:
        "选择本地模型(本地模型严重降智)":
            jump OllamaInput_label
        "选择使用deepseek api key":
            jump DeepSeekInput_label
    return


label OllamaInput_label:
    scene bg

    $ ollama_api_base = renpy.input("输入ollama默认api地址:http://localhost:11434/v1 。如果有更改，请自行调整:")
    $ ollama_api_base = ollama_api_base.strip()
    $ openai.api_base=ollama_api_base
    $ openai.api_key="ollama"# Ollama 不校验 key

    $ ollama_model_name = renpy.input("输入ollama模型名称,例如:deepseek-r1:8b,如果不清楚，请打开终端输入ollama list查看:")
    $ ollama_model_name = ollama_model_name.strip()

    $ renpy.pause(2.0, hard=True)

    menu OllamaCharacterSetting_menu:
        "默认设定":
            $ OllamaDefault_flag = True
            jump OllamaMurasameCustomize_label
        "自定义设定人物":
            jump OllamaMurasameCustomize_label
    
    return


label DeepSeekInput_label:
    scene bg

    $ api_key = renpy.input("输入api key:")  
    $ api_key = api_key.strip()
    $ openai.api_base = "https://api.deepseek.com"
    $ openai.api_key = api_key

    "默认设定和自定义设定都会消耗token!{nw=5}"
    $ renpy.pause(2.0, hard=True)

    menu DeepseekChoiceContinue_menu:
        "确认":
            jump DeepseekCharacterSetting_menu
        "回退":
            jump start
    

    menu DeepseekCharacterSetting_menu:
        "选择默认设定":
            $ DeepseeekDefault_flag = True
            jump DeepseekMurasameCustomize_label
        "自定义设定人物":
            jump DeepseekMurasameCustomize_label

    return


label OllamaMurasameCustomize_label:
    scene bg

    if OllamaDefault_flag:
        $ Default_character_setting_info = DefaultCharacterSetting_func()
        $ OllamaCharaterSetting_func(Default_character_setting_info) 
        "设定中，等待10秒，或者更多时间{nw=15}"
        $ renpy.pause(10.0, hard=True)

        if ollama_reply:
            "设定完成,点击屏幕继续"

        jump OllamaMurasameSpeak_label 

    else:
        $ user_input_character_setting = renpy.input("名字，昵称，服装，样貌已经设定好，可以自行设定背景:")
        $ user_input_character_setting = user_input_character_setting.strip()
        $ user_character_setting = CustomCharacterSetting_func(user_input_character_setting)
        $ OllamaCharaterSetting_func(user_character_setting)  

        "设定中，等待10秒，或者更多时间{nw=15}"
        $ renpy.pause(10.0, hard=True)

        if ollama_reply:
            "设定完成,点击屏幕继续"

        jump OllamaMurasameSpeak_label
    
    return


label DeepseekMurasameCustomize_label:
    scene bg

    if DeepseeekDefault_flag:
        $ Default_character_setting_info = DefaultCharacterSetting_func()
        $ DeepSeekCharaterSetting_func(Default_character_setting_info) 
        "设定中，等待10秒，或者更多时间{nw=15}"
        $ renpy.pause(10.0, hard=True)

        if deepseek_reply:
            "设定完成,点击屏幕继续"

        jump DeepseekMurasameSpeak_label 

    else:
        $ user_input_character_setting = renpy.input("名字，昵称，服装，样貌已经设定好，可以自行设定背景:")
        $ user_input_character_setting = user_input_character_setting.strip()
        $ user_character_setting = CustomCharacterSetting_func(user_input_character_setting)
        $ DeepSeekCharaterSetting_func(user_character_setting)  

        "设定中，等待10秒，或者更多时间{nw=15}"
        $ renpy.pause(10.0, hard=True)

        if deepseek_reply:
            "设定完成,点击屏幕继续"

        jump DeepseekMurasameSpeak_label

    return


label OllamaMurasameSpeak_label:
    play music [m1, m2, m3, m4, m5, m6] loop

    scene bg

    while True:
        show Murasame No_movement with dissolve


        $ user_input = renpy.input("对丛雨-Ollama说什么:")
        $ user_input = user_input.strip()

        if user_input:
            $ ollama_reply = None  # 清空上一次回复
            $ RequestOllamaResponse_func(user_input, ollama_model_name, ollama_conversation_history)
        
        "丛雨-Ollama: 思考中...(没出现文字可能是加载中或者模型问题){nw=10}"
        $ renpy.pause(5.0, hard=True)
        
        # 等待后台线程返回
        while ollama_reply is None:
            $ renpy.pause(0.5, hard=True)

        $ murasame_motion = RandomMurasameMotion_func()
        $ renpy.show("Murasame " + murasame_motion)
        with dissolve
        "[ollama_reply]"

        show Murasame No_movement with dissolve
    
    return  



label DeepseekMurasameSpeak_label:
    play music [m1, m2, m3, m4, m5, m6] loop

    scene bg

    while True:
        show Murasame No_movement with dissolve

        $ user_input = renpy.input("对丛雨-DeepSeek说什么:")
        $ user_input = user_input.strip()

        if user_input:
            $ RequestDeepseekResponse_func(user_input, deepseek_conversation_history)
            $ renpy.pause(0.5, hard=True)

        "丛雨-DeepSeek: 思考中...(没出现文字可能是加载中或者网络问题){nw=10}"
        $ renpy.pause(5.0, hard=True)

        while deepseek_reply is None:
            $ renpy.pause(0.5, hard=True)

        with dissolve
        $ murasame_motion = RandomMurasameMotion_func()
        $ renpy.show("Murasame " + murasame_motion)
        with dissolve
        "[deepseek_reply]"

        show Murasame No_movement with dissolve

    return  