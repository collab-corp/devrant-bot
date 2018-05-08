# -*- coding: utf-8 -*-

from chatterbot import ChatBot
chatbot = ChatBot("AiMee")

response = chatbot.get_response("Good morning!")
print(response)

from chatterbot import ChatBot

chatbot = ChatBot('natsuki-bot')

# Get a response to an input statement
chatbot.get_response("Hello, how are you today?")