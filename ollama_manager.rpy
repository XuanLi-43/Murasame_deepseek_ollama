init python:
    import openai
    import requests
    import json
    import threading
    import re

    ollama_reply = ""  #存储ollama回复

    ollama_conversation_history = []  #存储对话历史

    #openai.api_base="http://localhost:11434/v1",  # 指向 Ollama 本地 API
    #openai.api_key="ollama"                        # Ollama 不校验 key

    def RemoveThinkTagsAndClean_func(reply):
        # 使用正则表达式匹配并移除<think>标签及其内容
        cleaned_reply = re.sub(r'<think>.*?</think>', '', reply, flags=re.DOTALL)
        
        cleaned_reply = re.sub(r'\n\s*\n+', '\n\n', cleaned_reply)
        
        cleaned_reply = re.sub(r'^\s+|\s+$', '', cleaned_reply, flags=re.MULTILINE)
        
        cleaned_reply = re.sub(r' +', ' ', cleaned_reply)
        return cleaned_reply.strip()



    def OllamaCharaterSetting_func(charater_setting_info:str):
        #设置角色信息。存储在历史对话中
        ollama_conversation_history.append({"role": "system", "content": charater_setting_info})
    

    def CallOllamaApiAsync_func(user_input: str, ollama_model_name:str, ollama_conversation_history, callback):
        ollama_conversation_history.append({"role": "user", "content": user_input})  #添加用户输入到对话历史
        
        try:
            ollama_response = openai.ChatCompletion.create(
                model=ollama_model_name,
                messages=ollama_conversation_history,
                stream=False
            )
        
            reply = ollama_response.choices[0].message["content"]

            cleaned_reply = RemoveThinkTagsAndClean_func(reply)

            ollama_conversation_history.append({"role": "assistant", "content": cleaned_reply})
        except Exception as e:
            cleaned_reply = f"Ollama发生错误: {e}"
        
        #丢回主线程
        renpy.invoke_in_thread(lambda: callback(cleaned_reply))
    
    def RequestOllamaResponse_func(user_input: str, ollama_model_name:str, ollama_conversation_history):
        def OnOllamaResponseReceived_func(reply):
            global ollama_reply
            ollama_reply = reply
            # 重新触发交互，继续执行后续脚本
            renpy.restart_interaction()

        # 后台线程调用
        threading.Thread(
            target=CallOllamaApiAsync_func,
            args=(user_input, ollama_model_name, ollama_conversation_history, OnOllamaResponseReceived_func),
            daemon=True
        ).start()
