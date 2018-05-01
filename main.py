# -*- coding: utf-8 -*-

from chatterbot import ChatBot
chatbot = ChatBot("AiMee")

response = chatbot.get_response("Good morning!")
print(response)

