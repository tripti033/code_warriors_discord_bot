import random


def handle_response(message) -> str:
    p_message = message.lower()
    if p_message == 'hi':
        return 'Hey there!'

    if p_message == 'ping':
        return 'pong'

    if p_message == '!help':
        return "`sure! why not!`"

   
