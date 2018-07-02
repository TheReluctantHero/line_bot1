from linebot.models import (
    TextSendMessage, ImageSendMessage,
)
import random

def create_message(input):
    kakomon = ['過去問が欲しい']
    holly = ['01.jpg','02.jpg','03.jpg']
    horror = ['04.gif','05.gif','06.gif']
    if input not in kakomon:
        message = TextSendMessage('「過去問が欲しい」と入力してね')
    else:
        message = ImageSendMessage(
        preview_image_url = 'https://kakomon-bot.herokuapp.com/images/'+random.choice(holly),
        original_content_url = 'https://kakomon-bot.herokuapp.com/images/'+random.choice(horror)
    )

    return message
