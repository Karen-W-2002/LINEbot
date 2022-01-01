import os
import requests
import re

from bs4 import BeautifulSoup

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction
from linebot.models.actions import URIAction
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
                            label='Search other Recipes',
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

def send_chef_carousel(id):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text = "Carousel template",
        template = CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url = "https://www.biography.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cg_face%2Cq_auto:good%2Cw_300/MTgwOTcxNDk2NDQzNzQ5NzM2/gettyimages-1148433914.jpg",
                    title = "Chef #1",
                    text = "Gordon Ramsay",
                    actions=[
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
                        URIAction(
                            label='Website',
                            uri='https://orlandomurrin.com/'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = "https://ychef.files.bbci.co.uk/1600x900/p04tx3m6.webp",
                    title = "Navigation Menu",
                    text = "Navigate to the chef's recipes",
                    actions=[
                        MessageTemplateAction(
                            label='View Recipes',
                            text='show chef recipes'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = "https://media-cldnry.s-nbcnews.com/image/upload/t_fit-1240w,f_auto,q_auto:best/newscms/2017_05/1890591/170203-salt-bae-mn-1530.jpg",
                    title = "Navigation Menu",
                    text = "Navigate to the main menu",
                    actions=[
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
                    thumbnail_image_url = "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/lamb-biryani-83e5c3d.jpg?quality=90&webp=true&resize=440,400",
                    title = "Tom Kerridge",
                    text = "Lamb biryani",
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
                    thumbnail_image_url = "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/recipe-image-legacy-id-1001464_11-ed687dd.jpg?quality=90&webp=true&resize=440,400",
                    title = "Orlando Murrin",
                    text = "Best ever chocolate brownies recipe",
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
                    thumbnail_image_url="https://media-cldnry.s-nbcnews.com/image/upload/t_fit-1240w,f_auto,q_auto:best/newscms/2017_05/1890591/170203-salt-bae-mn-1530.jpg",
                    title="Navigation Menu",
                    text="Navigate to ... ",
                    actions=[
                        MessageTemplateAction(
                            label='Search other Recipes',
                            text='search other recipes'
                        ),
                        MessageTemplateAction(
                            label='Back to Recipes',
                            text='search recipes'
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

def send_showrecipe_carousel(id, imgs, titles, titletexts, labels, texts):
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
                        label=labels[0],
                        text=texts[0]
                    ),
                    MessageTemplateAction(
                        label=labels[1],
                        text=texts[1]
                    ),
                    MessageTemplateAction(
                        label=labels[2],
                        text=texts[2]
                    )
                ]
            )
        )

    cols.append(
        CarouselColumn(
            thumbnail_image_url="https://media-cldnry.s-nbcnews.com/image/upload/t_fit-1240w,f_auto,q_auto:best/newscms/2017_05/1890591/170203-salt-bae-mn-1530.jpg",
            title="Navigation Menu",
            text="Navigate to ... ",
            actions=[
                MessageTemplateAction(
                    label='Search other Recipes',
                    text='search other recipes'
                ),
                MessageTemplateAction(
                    label='Back to Recipes',
                    text='search recipes'
                ),
                MessageTemplateAction(
                    label='Back to Main Menu',
                    text='home'
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

def find_urls(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    a = []

    for results in soup.find_all(class_="standard-card-new__article-title", href = True):
        a.append("https://www.bbcgoodfood.com/" + results['href'])

    return a

def get_img_url(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    a = ""
    
    for result in soup.find("div", class_="post-header__image-container"):
        img = result.find_all(class_="image__img")
        for i in img:
            a = i.get('src')

    return a

def get_recipe_name(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="__next")
    job_elements = results.find_all("h1", class_="heading-1")

    a = ""

    for job_element in job_elements:
        a += job_element.text.strip()

    return a

def find_method(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="__next")
    job_elements = results.find_all("li", class_="pb-xs pt-xs list-item")

    a = ""

    for job_element in job_elements:
        new_elements = job_element.find_all("div", class_="editor-content")
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
    
