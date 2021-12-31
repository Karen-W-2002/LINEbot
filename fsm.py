from transitions.extensions import GraphMachine
from linebot.models import MessageTemplateAction

from utils import find_ingredient, find_method, find_nutrition, send_chef_carousel, send_cr_carousel, send_dinner_carousel, send_lunch_carousel, send_msg_carousel, send_text_message, send_button_message, send_recipe_carousel, send_bf_carousel, send_uri_carousel

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

    def is_going_to_showmethod(self, event):
        text = event.message.text
        return text.lower() == "show method"#grab show method and remove teh back

    def is_going_to_showingredient(self, event):
        text = event.message.text
        return text.lower() == "show ingredients"#

    def is_going_to_shownutrition(self, event):
        text = event.message.text
        return text.lower() == "show nutrition"#

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
        id = event.source.user_id
        send_chef_carousel(id)

    def on_enter_showbreakfast(self, event):
        id = event.source.user_id
        send_bf_carousel(id)

    def on_enter_showlunch(self, event):
        id = event.source.user_id
        send_lunch_carousel(id)

    def on_enter_showdinner(self, event):
        id = event.source.user_id
        send_dinner_carousel(id)

    def on_enter_showchefrecipes(self, event):
        id = event.source.user_id
        send_cr_carousel(id)

    def on_enter_showmethod(self, event):
        id = event.source.user_id
        reply_token = event.reply_token

        imgs = ["https://fooduncut.com/wp-content/uploads/2021/08/Chinese-Cooking-Hacks.jpg",
        "https://esmmweighless.com/wp-content/uploads/2019/12/Carolyn-Cooking-Blog.jpg",
        "https://goodfoodireland.ie/wp-content/uploads/2021/04/copy-of-copy-of-untitled-1.jpg"]
        titles = ["Navigation Menu", "Navigation Menu", "Navigation Menu"]
        titletexts = ["Navigate to the recipe menu", "Navigate to the ingredient list", "Navigate to the nutrition facts"]
        labels = ["Back to Recipes", "Look up Ingredients", "Look up Nutrition"]
        texts = ["search recipes", "show ingredients", "show nutrition"]

        send_msg_carousel(id, imgs, titles, titletexts, labels, texts)
        send_text_message(reply_token, find_method("https://www.bbcgoodfood.com/recipes/beef-wellington")) ## CHANGE URL

    def on_enter_showingredient(self, event):
        id = event.source.user_id
        reply_token = event.reply_token

        imgs = ["https://fooduncut.com/wp-content/uploads/2021/08/Chinese-Cooking-Hacks.jpg",
        "https://esmmweighless.com/wp-content/uploads/2019/12/Carolyn-Cooking-Blog.jpg",
        "https://goodfoodireland.ie/wp-content/uploads/2021/04/copy-of-copy-of-untitled-1.jpg"]
        titles = ["Navigation Menu", "Navigation Menu", "Navigation Menu"]
        titletexts = ["Navigate to the recipe menu", "Navigate to the cooking method", "Navigate to the nutrition facts"]
        labels = ["Back to Recipes", "Look up Method", "Look up Nutrition"]
        texts = ["search recipes", "show method", "show nutrition"]

        send_msg_carousel(id, imgs, titles, titletexts, labels, texts)
        send_text_message(reply_token, find_ingredient("https://www.bbcgoodfood.com/recipes/beef-wellington")) ## CHANGE URL

    def on_enter_shownutrition(self, event):
        id = event.source.user_id

        imgs = ["https://fooduncut.com/wp-content/uploads/2021/08/Chinese-Cooking-Hacks.jpg",
        "https://esmmweighless.com/wp-content/uploads/2019/12/Carolyn-Cooking-Blog.jpg",
        "https://goodfoodireland.ie/wp-content/uploads/2021/04/copy-of-copy-of-untitled-1.jpg"]
        titles = ["Navigation Menu", "Navigation Menu", "Navigation Menu"]
        titletexts = ["Navigate to the recipe menu", "Navigate to the cooking method", "Navigate to the ingredient list"]
        labels = ["Back to Recipes", "Look up Method", "Look up Ingredients"]
        texts = ["search recipes", "show method", "show ingredients"]

        n_imgs = ["https://c4.wallpaperflare.com/wallpaper/771/184/50/spongebob-squarepants-wallpaper-preview.jpg",
        "https://i.pinimg.com/564x/32/0d/c2/320dc2e12cd1c45cd9d6dd50464ee4f9.jpg",
        "https://i.pinimg.com/564x/e6/7f/25/e67f2518d5c517c93890eacd0964daf5.jpg",
        "https://pbs.twimg.com/media/D6ymCLrXsAIjspC?format=jpg&name=small",
        "https://i.pinimg.com/564x/db/a1/66/dba1667ede306ca32c0b2fdf303d2346.jpg",
        "https://www.shitpostbot.com/img/sourceimages/fiber-57de2d2707550.jpeg",
        "https://i.pinimg.com/564x/3d/6b/e4/3d6be4592e7acae3e4c6796954a0df0b.jpg",
        "https://www.wateraid.org/uk/sites/g/files/jkxoof211/files/styles/full_grid_image_2x/public/spongebob-dried-out-in-a-particularly-water-scarce-moment.jpg?itok=DWFZowSP",
        ]
        n_titles = ["KCAL", "FAT", "SATURATES", "CARBS", "SUGARS", "FIBRE", "PROTEIN", "SALT"]
        nutrition_num = find_nutrition("https://www.bbcgoodfood.com/recipes/soft-boiled-eggs") ## CHANGE URL
        n_labels = ["Learn More", "Learn More", "Learn More", "Learn More", "Learn More", "Learn More", "Learn More", "Learn More"] 
        n_uris = ["https://www.medicalnewstoday.com/articles/263028",
        "https://www.medicalnewstoday.com/articles/141442",
        "https://www.medicalnewstoday.com/articles/321655",
        "https://www.medicalnewstoday.com/articles/161547#:~:text=Carbohydrates%20are%20the%20main%20source,mainly%20found%20in%20plant%20foods.",
        "https://www.medicalnewstoday.com/articles/does-your-body-need-sugar",
        "https://www.medicalnewstoday.com/articles/146935#:~:text=Dietary%20fiber%2C%20also%20known%20as,%2C%20whole%20grains%2C%20and%20legumes.",
        "https://www.medicalnewstoday.com/articles/196279",
        "https://www.medicalnewstoday.com/articles/146677#sources"
        ]

        send_msg_carousel(id, imgs, titles, titletexts, labels, texts)
        send_uri_carousel(id, n_imgs, n_titles, nutrition_num, n_labels, n_uris)