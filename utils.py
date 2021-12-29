import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction
from linebot.models.actions import PostbackAction
from linebot.models.template import CarouselColumn, CarouselTemplate


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)

def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def send_image_url(id, img_url):
    pass

def send_button_message(id, img, title, text, buttons):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text = "Buttons template of " + title,
        template = ButtonsTemplate(
            thumbnail_image_url = img,
            title = title,
            text = text,
            actions = buttons
        )
    )

    line_bot_api.push_message(id, message)
    return "OK"

def send_recipe_carousel(id):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text = "Carousel template of Recipe Menu",
        template = CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url = "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/american-pancakes-5fc705c.jpg?quality=90&webp=true&resize=440,400",
                    title = "Recipe Menu #1",
                    text = "Which recipe category would you like to view?",
                    actions=[
                        MessageTemplateAction(
                            label='Breakfast',
                            text='show breakfast'
                        ),
                        MessageTemplateAction(
                            label='Lunch',
                            text='show lunch'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = "https://images.immediate.co.uk/production/volatile/sites/30/2021/06/Miso-mushroom-and-halloumi-burgers-a1f5a05.jpg?quality=90&webp=true&resize=900,817",
                    title = "Recipe Menu #2",
                    text = "Which recipe category would you like to view?",
                    actions=[
                        MessageTemplateAction(
                            label='Dinner',
                            text='show dinner'
                        ),
                        MessageTemplateAction(
                            label='Chef Recipes',
                            text='show chef recipes'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/dessert-main-image-molten-cake-0fbd4f2.jpg?quality=90&webp=true&resize=500,454",
                    title = "Recipe Menu #3",
                    text = "Which recipe category would you like to view?",
                    actions=[
                        MessageTemplateAction(
                            label='Search others',
                            text='search other recipes'
                        ),
                        MessageTemplateAction(
                            label='Back to Main Menu',
                            text='home'
                        )
                    ]
                )
            ]
        )
    )

    line_bot_api.push_message(id, message)
    return "OK"

def send_bf_carousel(id):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text = "Carousel template of Breakfast Menu",
        template = CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url = "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/american-style-pancakes-87119e3.jpg?quality=90&webp=true&resize=440,400",
                    title = "Breakfast #1",
                    text = "American pancakes",
                    actions=[
                        MessageTemplateAction(
                            label='Cooking Method',
                            text='cooking method'
                        ),
                        MessageTemplateAction(
                            label='Ingredients',
                            text='todo...'
                        ),
                        MessageTemplateAction(
                            label='Nutrition',
                            text='todo...'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/eggsoldiers-f0e097c.jpg?quality=90&webp=true&resize=440,400",
                    title = "Breakfast #2",
                    text = "Soft-boiled eggs",
                    actions=[
                        MessageTemplateAction(
                            label='Cooking Method',
                            text='todo...'
                        ),
                        MessageTemplateAction(
                            label='Ingredients',
                            text='todo...'
                        ),
                        MessageTemplateAction(
                            label='Nutrition',
                            text='todo...'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/overnight-oats-32a2747.jpg?quality=90&webp=true&resize=440,400",
                    title = "Breakfast #3",
                    text = "Overnight oats",
                    actions=[
                        MessageTemplateAction(
                            label='Cooking Method',
                            text='todo...'
                        ),
                        MessageTemplateAction(
                            label='Ingredients',
                            text='todo...'
                        ),
                        MessageTemplateAction(
                            label='Nutrition',
                            text='todo...'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/overnight-oats-32a2747.jpg?quality=90&webp=true&resize=440,400",
                    title = "Breakfast #3",
                    text = "Overnight oats",
                    actions=[
                        MessageTemplateAction(
                            label='Search others',
                            text='todo...'
                        ),
                        MessageTemplateAction(
                            label='Back to Recipes',
                            text='todo...'
                        ),
                        MessageTemplateAction(
                            label='Back to Main Menu',
                            text='todo...'
                        )
                    ]
                )
            ]
        )
    )

    line_bot_api.push_message(id, message)
    return "OK"

def send_breakfast_carousel(id):
    pass

def send_breakfast_carousel(id):
    pass

def send_breakfast_carousel(id):
    pass