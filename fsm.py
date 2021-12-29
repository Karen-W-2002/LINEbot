from transitions.extensions import GraphMachine
from linebot.models import MessageTemplateAction

from utils import send_text_message, send_button_message, send_recipe_carousel, send_bf_carousel

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_start(self, event):
        text = event.message.text # This means whoever has the bot can enter anything to start it
        return True

    def is_going_to_searchrecipe(self, event):
        text = event.message.text
        return text.lower() == "search recipes"

    def is_going_to_searchnews(self, event):
        text = event.message.text
        return text.lower() == "search news"

    def is_going_to_searchchef(self, event):
        text = event.message.text
        return text.lower() == "search chefs"

    def is_going_to_showbreakfast(self, event):
        text = event.message.text
        return text.lower() == "show breakfast"

    def is_going_to_showlunch(self, event):
        text = event.message.text
        return text.lower() == "show lunch"
    
    def is_going_to_showdinner(self, event):
        text = event.message.text
        return text.lower() == "show dinner"
    
    def is_going_to_showchefrecipes(self, event):
        text = event.message.text
        return text.lower() == "show chef recipes"

    def on_enter_start(self, event):
        print("You entered start, you can search: recipe, news, chef or misc")

        id = event.source.user_id
        img = "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/chorizo-mozarella-gnocchi-bake-cropped-9ab73a3.jpg?quality=90&webp=true&resize=600,545"
        title = "Cooking Menu"
        text = "What are you looking for today?"
        buttons = [
            MessageTemplateAction(
                label = 'Recipes',
                text = 'search recipes'
            ),
            MessageTemplateAction(
                label = 'News',
                text = 'search news'
            ),
            MessageTemplateAction(
                label = 'Chefs',
                text = 'search chefs'
            )
        ]

        send_button_message(id, img,title, text, buttons)

    def on_enter_searchrecipe(self, event):
        id = event.source.user_id
        send_recipe_carousel(id)

    def on_enter_searchnews(self, event):
        print("search news...")

        reply_token = event.reply_token
        send_text_message(reply_token, "Entered news section")

    def on_enter_searchchef(self, event):
        print("search chefs...")

        reply_token = event.reply_token
        send_text_message(reply_token, "Entered chef section")

        reply_token = event.reply_token
        send_text_message(reply_token, "Entered misc section")

    def on_enter_showbreakfast(self, event):
        id = event.source.user_id
        send_bf_carousel(id)

    def on_enter_showlunch(self, event):
        print("showing lunch")

    def on_enter_showdinner(self, event):
        print("showing dinner")

    def on_enter_showchefrecipes(self, event):
        print("showing chef recipes")

"""
    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state1")
        #self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state2")
        #self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")
"""