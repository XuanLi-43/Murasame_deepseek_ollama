init python:
    import openai
    import requests
    import json
    import threading

    deepseek_reply = ""  #存储deepseek回复

    deepseek_conversation_history = []  #存储对话历史

    #openai.api_key = api_key 
    #openai.api_base = "https://api.deepseek.com"

    def DeepSeekCharaterSetting_func(charater_setting_info:str):
        #设置角色信息。存储在历史对话中
        deepseek_conversation_history.append({"role": "system", "content": charater_setting_info})  #设置全局人物信息


    def CallDeepseekApiAsync_func(user_input: str, deepseek_conversation_history, callback):
        deepseek_conversation_history.append({"role": "user", "content": user_input})  #添加用户输入到对话历史
        
        try:
            deepseek_response = openai.ChatCompletion.create(
                model="deepseek-chat",
                messages=deepseek_conversation_history,
                stream=False
            )
        
            reply = deepseek_response.choices[0].message["content"]
            deepseek_conversation_history.append({"role": "assistant", "content": reply})
        except Exception as e:
            reply = f"DeepSeek API 发生错误: {e}"
        
        # 回调丢回主线程
        renpy.invoke_in_thread(lambda: callback(reply))


    def RequestDeepseekResponse_func(user_input: str, deepseek_conversation_history):
        def OnDeepseekResponseReceived_func(reply):
            global deepseek_reply
            deepseek_reply = reply
            # 重新触发交互，继续执行后续脚本
            renpy.restart_interaction()

        # 后台线程调用
        threading.Thread(
            target=CallDeepseekApiAsync_func,
            args=(user_input, deepseek_conversation_history, OnDeepseekResponseReceived_func),
            daemon=True
        ).start()