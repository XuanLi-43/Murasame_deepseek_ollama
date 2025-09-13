# Murasame_deepseek_ollama
安装和使用: 
本地模型需要安装ollama，然后安装模型使用(本地模型比较蠢,容易乱回答,将就的用吧)
ollama下载地址:https://ollama.com/   

如果选择deepseek api key, 需要前往该平台购买
https://platform.deepseek.com/

# 目前情况
基于调用deepseek和ollama的简单聊天游戏
目前这个是半成品，不过起码能动了
用来练习的
之后会接入GPT-sovits,这样输出文本的同时还能讲话

# 该聊天游戏的原理
1. 写好一份初设设定，用于人物角色扮演
2. 调用deepseek或者ollama的api地址
3. 把这个初设设定,即Murasame_Default.txt或者Murasame_Basic.txt扔给语言模型，然后用列表存储起来
4. 扔完之后，就可以进行后续的回答了，将列表数据不停的扔给语言模型。
5. 语言模型输出的文本，提取出来就能显示在游戏内了

# 文件的主要内容
live2d---放live2d模型。
python-packages---放一些必要的库。
audio---放bgm。
images---背景图,
global_var.rpy ---一些必要的变量。
character_setting.rpy ---用于人物设定。
character_sound_manager.rpy ---请输入文本,还没搞。
deepseek_manager.rpy --- 调用deepseek,和存储数据。
ollama_manager.rpy--- 调用ollama,和存储数据。
script.rpy--- 内容。
Murasame_Basic.txt ---基本设定，通过character_setting.rpy,就可以自定义背景了。
Murasame_Default.txt--- 默认设定。

# live2d模型
丛雨的live2d模型:https://www.bilibili.com/video/BV1mb4y1i7xu
感谢@穿越电线 up主免费提供的模型

本项目仅作为学习与练习使用, 游戏内的人物角色，bgm,背景归柚子社所有，本人仅为二创
