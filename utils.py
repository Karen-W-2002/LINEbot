import os
import requests
import re

from bs4 import BeautifulSoup

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction
from linebot.models.actions import PostbackAction, URIAction
from linebot.models.template import CarouselColumn, CarouselTemplate, ImageCarouselColumn, ImageCarouselTemplate


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

def send_news_carousel(id):
    pass

def send_chef_carousel(id):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text = "Carousel template of Chefs",
        template = CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url = "https://www.biography.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cg_face%2Cq_auto:good%2Cw_300/MTgwOTcxNDk2NDQzNzQ5NzM2/gettyimages-1148433914.jpg",
                    title = "Chef #1",
                    text = "Gordon Ramsay",
                    actions=[
                        MessageTemplateAction(
                            label='Personal Bio',
                            text='personal bio'
                        ),
                        MessageTemplateAction(
                            label='View Recipes',
                            text='show chef recipes'
                        ),
                        URIAction(
                            label='Website',
                            uri='https://www.gordonramsay.com/'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = "https://i.guim.co.uk/img/media/3a22e79db975a2eaa13bca0a25b0651fc42c7cde/186_719_5455_3273/master/5455.jpg?width=620&quality=45&auto=format&fit=max&dpr=2&s=a2c69aaf4a92813d80d5d6ee04d7ce60",
                    title = "Chef #2",
                    text = "Tom Kerridge",
                    actions=[
                        MessageTemplateAction(
                            label='Personal Bio',
                            text='personal bio'
                        ),
                        MessageTemplateAction(
                            label='View Recipes',
                            text='show chef recipes'
                        ),
                        URIAction(
                            label='Website',
                            uri='https://tomkerridge.com/'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = "https://pbs.twimg.com/profile_images/445255599400304640/RZaNE7-J_400x400.jpeg",
                    title = "Chef #3",
                    text = "Orlando Murrin",
                    actions=[
                        MessageTemplateAction(
                            label='Personal Bio',
                            text='personal bio'
                        ),
                        MessageTemplateAction(
                            label='View Recipes',
                            text='show chef recipes'
                        ),
                        URIAction(
                            label='Website',
                            uri='https://orlandomurrin.com/'
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
                            text='show method'
                        ),
                        MessageTemplateAction(
                            label='Ingredients',
                            text='show ingredients'
                        ),
                        MessageTemplateAction(
                            label='Nutrition',
                            text='show nutrition'
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
                            text='show method'
                        ),
                        MessageTemplateAction(
                            label='Ingredients',
                            text='show ingredients'
                        ),
                        MessageTemplateAction(
                            label='Nutrition',
                            text='show nutrition'
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
                            text='show method'
                        ),
                        MessageTemplateAction(
                            label='Ingredients',
                            text='show ingredients'
                        ),
                        MessageTemplateAction(
                            label='Nutrition',
                            text='show nutrition'
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
                            text='todo'
                        ),
                        MessageTemplateAction(
                            label='Back to Recipes',
                            text='search recipes'
                        ),
                        MessageTemplateAction(
                            label='Back to Main Menu',
                            text='change...'
                        )
                    ]
                )
            ]
        )
    )

    line_bot_api.push_message(id, message)
    return "OK"

def send_lunch_carousel(id):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text = "Carousel template of Lunch Menu",
        template = CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url = "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/recipe-image-legacy-id-1035613_10-0e544b7.jpg?quality=90&webp=true&resize=500,454",
                    title = "Lunch #1",
                    text = "Chicken noodle soup",
                    actions=[
                        MessageTemplateAction(
                            label='Cooking Method',
                            text='show method'
                        ),
                        MessageTemplateAction(
                            label='Ingredients',
                            text='show ingredients'
                        ),
                        MessageTemplateAction(
                            label='Nutrition',
                            text='show nutrition'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/lentil_soup-c6fa61c.jpg?quality=90&webp=true&resize=440,400",
                    title = "Lunch #2",
                    text = "Lentil soup",
                    actions=[
                        MessageTemplateAction(
                            label='Cooking Method',
                            text='show method'
                        ),
                        MessageTemplateAction(
                            label='Ingredients',
                            text='show ingredients'
                        ),
                        MessageTemplateAction(
                            label='Nutrition',
                            text='show nutrition'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/seafood_pasta-f15956d.jpg?quality=90&webp=true&resize=500,454",
                    title = "Lunch #3",
                    text = "20-minute seafood pasta",
                    actions=[
                        MessageTemplateAction(
                            label='Cooking Method',
                            text='show method'
                        ),
                        MessageTemplateAction(
                            label='Ingredients',
                            text='show ingredients'
                        ),
                        MessageTemplateAction(
                            label='Nutrition',
                            text='show nutrition'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/overnight-oats-32a2747.jpg?quality=90&webp=true&resize=440,400",
                    title = "Lunch #3",
                    text = "Overnight oats",
                    actions=[
                        MessageTemplateAction(
                            label='Search others',
                            text='todo'
                        ),
                        MessageTemplateAction(
                            label='Back to Recipes',
                            text='search recipes'
                        ),
                        MessageTemplateAction(
                            label='Back to Main Menu',
                            text='change...'
                        )
                    ]
                )
            ]
        )
    )

    line_bot_api.push_message(id, message)
    return "OK"

def send_dinner_carousel(id):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text = "Carousel template of Dinner Menu",
        template = CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url = "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/sausage-ragu-a4e1460.jpg?quality=90&webp=true&resize=440,400",
                    title = "Dinner #1",
                    text = "Sausage ragu",
                    actions=[
                        MessageTemplateAction(
                            label='Cooking Method',
                            text='show method'
                        ),
                        MessageTemplateAction(
                            label='Ingredients',
                            text='show ingredients'
                        ),
                        MessageTemplateAction(
                            label='Nutrition',
                            text='show nutrition'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/beef-curry-711a4c1.jpg?quality=90&webp=true&resize=440,400",
                    title = "Dinner #2",
                    text = "Beef curry",
                    actions=[
                        MessageTemplateAction(
                            label='Cooking Method',
                            text='show method'
                        ),
                        MessageTemplateAction(
                            label='Ingredients',
                            text='show ingredients'
                        ),
                        MessageTemplateAction(
                            label='Nutrition',
                            text='show nutrition'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/salmon-leek-parcel-6dd60f6.jpg?quality=90&webp=true&resize=400,363",
                    title = "Dinner #3",
                    text = "Salmon & leek parcel",
                    actions=[
                        MessageTemplateAction(
                            label='Cooking Method',
                            text='show method'
                        ),
                        MessageTemplateAction(
                            label='Ingredients',
                            text='show ingredients'
                        ),
                        MessageTemplateAction(
                            label='Nutrition',
                            text='show nutrition'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/salmon-leek-parcel-6dd60f6.jpg?quality=90&webp=true&resize=400,363",
                    title = "Lunch #3",
                    text = "Overnight oats",
                    actions=[
                        MessageTemplateAction(
                            label='Search others',
                            text='todo'
                        ),
                        MessageTemplateAction(
                            label='Back to Recipes',
                            text='search recipes'
                        ),
                        MessageTemplateAction(
                            label='Back to Main Menu',
                            text='change...'
                        )
                    ]
                )
            ]
        )
    )

    line_bot_api.push_message(id, message)
    return "OK"

def send_cr_carousel(id):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text = "Carousel template of Chef Recipes Menu",
        template = CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url = "https://images.immediate.co.uk/production/volatile/sites/30/2012/09/Beef-wellington-d4f3320.jpg?quality=90&webp=true&resize=600,545",
                    title = "Gordon Ramsay",
                    text = "Beef wellington",
                    actions=[
                        MessageTemplateAction(
                            label='Cooking Method',
                            text='show method'
                        ),
                        MessageTemplateAction(
                            label='Ingredients',
                            text='show ingredients'
                        ),
                        MessageTemplateAction(
                            label='Nutrition',
                            text='show nutrition'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/salmon-leek-parcel-6dd60f6.jpg?quality=90&webp=true&resize=400,363",
                    title = "Lunch #3",
                    text = "Overnight oats",
                    actions=[
                        MessageTemplateAction(
                            label='Search chefs',
                            text='search chefs'
                        ),
                        MessageTemplateAction(
                            label='Back to Recipes',
                            text='search recipes'
                        ),
                        MessageTemplateAction(
                            label='Back to Main Menu',
                            text='change...'
                        )
                    ]
                )
            ]
        )
    )

    line_bot_api.push_message(id, message)
    return "OK"

def send_msg_carousel(id, imgs, titles, titletexts, labels, texts):
    line_bot_api = LineBotApi(channel_access_token)

    cols = []
    for i, imgurl in enumerate(imgs):
        cols.append(
            CarouselColumn(
                thumbnail_image_url=imgurl,
                title=titles[i],
                text=titletexts[i],
                actions=[
                    MessageTemplateAction(
                        label=labels[i],
                        text=texts[i]
                    )
                ]
            )
        )

    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(columns=cols)
    )

    line_bot_api.push_message(id, message)
    return "OK"

def send_uri_carousel(id, imgs, titles, titletexts, labels, uris):
    line_bot_api = LineBotApi(channel_access_token)

    cols = []
    for i, imgurl in enumerate(imgs):
        cols.append(
            CarouselColumn(
                thumbnail_image_url=imgurl,
                title=titles[i],
                text=titletexts[i],
                actions=[
                    URIAction(
                        label=labels[i],
                        uri=uris[i]
                    )
                ]
            )
        )

    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(columns=cols)
    )

    line_bot_api.push_message(id, message)
    return "OK"

# WEB SCRAPER FUNCTIONS

def find_method(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="__next")
    job_elements = results.find_all("li", class_="pb-xs pt-xs list-item")

    a = ""

    for job_element in job_elements:
        new_elements = job_element.find_all("div",class_="editor-content")
        for new_element in new_elements:
            a+= "⭐️" + new_element.text.strip() + "\n"

    return a.strip()

def find_ingredient(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="__next")
    job_elements = results.find_all("li", class_="pb-xxs pt-xxs list-item list-item--separator")

    a = ""

    for job_element in job_elements:
        a += "⭐️" + job_element.text.strip() + "\n"

    return a.strip()

def find_nutrition(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="__next")
    job_elements = results.find_all("tr", class_="key-value-blocks__item")

    a = []
    
    for job_element in job_elements:
        res = re.sub("[A-Za-z]+", lambda ele: ele[0] + " ", job_element.text.strip())
        a.append(res)

    return a
    
