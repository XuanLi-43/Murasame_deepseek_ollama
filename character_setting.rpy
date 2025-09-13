#默认人物设定和自定义人物设定
init python:
    def DefaultCharacterSetting_func():
        with renpy.open_file('Murasame_Default.txt', encoding='utf-8') as Murasame_Default :
            Default_character_setting_info = Murasame_Default.read()
            return Default_character_setting_info
        


    def CustomCharacterSetting_func(user_input_character_setting:str):
        with renpy.open_file('Murasame_Basic.txt', encoding='utf-8') as Murasame_Basic:
            character_setting_basic = Murasame_Basic.read()
            user_character_setting = user_input_character_setting + character_setting_basic
            return user_character_setting