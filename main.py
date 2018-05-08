# -*- coding: utf-8 -*-

from chatterbot import ChatBot

chatbot = ChatBot('natsuki-bot')

# initial message to user, played once
print("Natsuki> Natsuki bot here")

# Get a response to an input statement
response = chatbot.get_response(
    input())

print("Natsuki> ", response)

