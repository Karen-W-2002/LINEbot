from linebot.models.events import PostbackEvent
from transitions.extensions import GraphMachine
from linebot.models import MessageTemplateAction

from utils import find_ingredient, find_method, find_nutrition, find_urls, get_img_url, get_recipe_name, send_chef_carousel, send_cr_carousel, send_msg_carousel, send_showrecipe_carousel, send_text_message, send_button_message, send_recipe_carousel, send_uri_carousel

class TocMachine(GraphMachine):
    currenturl = ""

    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_start(self, event):
        # This means whoever has the bot can enter anything to start it
        return True

    def is_going_to_searchrecipe(self, event):
        if not isinstance(event, PostbackEvent):
            text = event.message.text
            return text.lower() == "search recipes"
        else:
            return False

    def is_going_to_searchchef(self, event):
        if not isinstance(event, PostbackEvent):
            text = event.message.text
            return text.lower() == "search chefs"
        else:
            return False

    def is_going_to_showbreakfast(self, event):
        if not isinstance(event, PostbackEvent):
            text = event.message.text
            return text.lower() == "show breakfast"
        else:
            return False

    def is_going_to_showlunch(self, event):
        if not isinstance(event, PostbackEvent):
            text = event.message.text
            return text.lower() == "show lunch"
        else:
            return False
    
    def is_going_to_showdinner(self, event):
        if not isinstance(event, PostbackEvent):
            text = event.message.text
            return text.lower() == "show dinner"
        else:
            return False
    
    def is_going_to_showchefrecipes(self, event):
        if not isinstance(event, PostbackEvent):
            text = event.message.text
            return text.lower() == "show chef recipes"
        else:
            return False

    def is_going_to_showmethod(self, event):
        if not isinstance(event, PostbackEvent):
            text = event.message.text
            return text.lower() == "show method"
        else:
            data = event.postback.data.split('&')
            self.currenturl = data[0]
            return data[1].lower() == "show method"

    def is_going_to_showingredient(self, event):
        if not isinstance(event, PostbackEvent):
            text = event.message.text
            return text.lower() == "show ingredients"
        else:
            data = event.postback.data.split('&')
            self.currenturl = data[0]
            return data[1].lower() == "show ingredients"

    def is_going_to_shownutrition(self, event):
        if not isinstance(event, PostbackEvent):
            text = event.message.text
            return text.lower() == "show nutrition"
        else:
            data = event.postback.data.split('&')
            self.currenturl = data[0]
            return data[1].lower() == "show nutrition"

    def is_going_to_searchotherrecipe(self, event):
        if not isinstance(event, PostbackEvent):
            text = event.message.text 
            return text.lower() == "search other recipes"
        else:
            return False

    def is_going_to_showother(self, event):
        if not isinstance(event, PostbackEvent):
            text = event.message.text
            if text.lower() == "home":
                return False
            else:
                return True
        else:
            return False

    def on_enter_start(self, event):
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
                label = 'Search for Recipes',
                text = 'search other recipes'
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

    def on_enter_searchchef(self, event):
        id = event.source.user_id
        send_chef_carousel(id)

    def on_enter_showbreakfast(self, event):
        id = event.source.user_id

        imgs = ["https://images.immediate.co.uk/production/volatile/sites/30/2020/08/vegan-banana-bread-ce14fcd.jpg?quality=90&webp=true&resize=440,400",
            "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/banana-muffins-943f3dc.jpg?quality=90&webp=true&resize=440,400",
            "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/pancakes-for-one-597b7c1.jpg?quality=90&webp=true&resize=440,400",
            "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/tofu_scramble-eaa0c64.jpg?quality=90&webp=true&resize=440,400"
        ]
        titles = []
        titletexts = ["Vegan banana bread", "Easy banana muffins", "Pancakes for one", "Tofu scramble"]
        labels = ["Cooking Method", "Ingredients", "Nutrition"]
        texts = ["show method", "show ingredients", "show nutrition"]
        datalist = ["https://www.bbcgoodfood.com/recipes/vegan-banana-bread",
            "https://www.bbcgoodfood.com/recipes/banana-muffins",
            "https://www.bbcgoodfood.com/recipes/pancakes-one",
            "https://www.bbcgoodfood.com/recipes/tofu-scramble"
        ]

        for i in range(4):
            titles.append("Breakfast #" + str(i+1))

        send_showrecipe_carousel(id, imgs, titles, titletexts, labels, texts, datalist)

    def on_enter_showlunch(self, event):
        id = event.source.user_id
        
        imgs = ["https://images.immediate.co.uk/production/volatile/sites/30/2020/08/roasted-sweet-potato-carrot-soup-1223acc.jpg?quality=90&webp=true&resize=440,400",
            "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/marghuerita-6e61fd5.jpg?quality=90&webp=true&resize=440,400",
            "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/cheats-chicken-ramen-d07e7ea.jpg?quality=90&webp=true&resize=440,400",
            "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/lentil-kofta-with-orzo-feta-5581f16-scaled.jpg?quality=90&webp=true&resize=600,545"
        ]
        titles = []
        titletexts = ["Roasted sweet potato & carrot soup", "Next level Margherita pizza", "Cheat's chicken ramen", "Lentil kofta with orzo & feta"]
        labels = ["Cooking Method", "Ingredients", "Nutrition"]
        texts = ["show method", "show ingredients", "show nutrition"]
        datalist = ["https://www.bbcgoodfood.com/recipes/roasted-sweet-potato-carrot-soup",
            "https://www.bbcgoodfood.com/recipes/next-level-margherita-pizza",
            "https://www.bbcgoodfood.com/recipes/cheats-chicken-ramen",
            "https://www.bbcgoodfood.com/recipes/lentil-kofta-orzo-feta"
        ]

        for i in range(4):
            titles.append("Lunch #" + str(i+1))

        send_showrecipe_carousel(id, imgs, titles, titletexts, labels, texts, datalist)

    def on_enter_showdinner(self, event):
        id = event.source.user_id

        imgs = ["https://images.immediate.co.uk/production/volatile/sites/30/2020/08/gnocchi-1d16725.jpg?quality=90&webp=true&resize=440,400",
            "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/recipe-image-legacy-id-52074_11-ca58d45.jpg?quality=90&webp=true&resize=440,400",
            "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/salmon-leek-parcel-6dd60f6.jpg?quality=90&webp=true&resize=400,363",
            "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/sausage-ragu-a4e1460.jpg?quality=90&webp=true&resize=440,400"
        ]
        titles = []
        titletexts = ["Chorizo & mozzarella gnocchi bake", "Mushroom risotto", "Salmon & leek parcel", "Sausage ragu"]
        labels = ["Cooking Method", "Ingredients", "Nutrition"]
        texts = ["show method", "show ingredients", "show nutrition"]
        datalist = ["https://www.bbcgoodfood.com/recipes/chorizo-mozzarella-gnocchi-bake",
            "https://www.bbcgoodfood.com/recipes/mushroom-risotto",
            "https://www.bbcgoodfood.com/recipes/salmon-leek-parcel",
            "https://www.bbcgoodfood.com/recipes/sausage-ragu"
        ]

        for i in range(4):
            titles.append("Dinner #" + str(i+1))

        send_showrecipe_carousel(id, imgs, titles, titletexts, labels, texts, datalist)

    def on_enter_showchefrecipes(self, event):
        id = event.source.user_id
        send_cr_carousel(id)

    def on_enter_showmethod(self, event):
        id = event.source.user_id
        reply_token = event.reply_token

        imgs = ["https://fooduncut.com/wp-content/uploads/2021/08/Chinese-Cooking-Hacks.jpg",
            "https://esmmweighless.com/wp-content/uploads/2019/12/Carolyn-Cooking-Blog.jpg",
            "https://goodfoodireland.ie/wp-content/uploads/2021/04/copy-of-copy-of-untitled-1.jpg"
        ]
        titles = ["Navigation Menu", "Navigation Menu", "Navigation Menu"]
        titletexts = ["Navigate to the recipe menu", "Navigate to the ingredient list", "Navigate to the nutrition facts"]
        labels = ["Back to Recipes", "Look up Ingredients", "Look up Nutrition"]
        texts = ["search recipes", "show ingredients", "show nutrition"]

        send_msg_carousel(id, imgs, titles, titletexts, labels, texts)
        send_text_message(reply_token, "🍴" + get_recipe_name(self.currenturl) + "\n\n" + find_method(self.currenturl))

    def on_enter_showingredient(self, event):
        id = event.source.user_id
        reply_token = event.reply_token

        imgs = ["https://fooduncut.com/wp-content/uploads/2021/08/Chinese-Cooking-Hacks.jpg",
            "https://esmmweighless.com/wp-content/uploads/2019/12/Carolyn-Cooking-Blog.jpg",
            "https://goodfoodireland.ie/wp-content/uploads/2021/04/copy-of-copy-of-untitled-1.jpg"
        ]
        titles = ["Navigation Menu", "Navigation Menu", "Navigation Menu"]
        titletexts = ["Navigate to the recipe menu", "Navigate to the cooking method", "Navigate to the nutrition facts"]
        labels = ["Back to Recipes", "Look up Method", "Look up Nutrition"]
        texts = ["search recipes", "show method", "show nutrition"]

        send_msg_carousel(id, imgs, titles, titletexts, labels, texts)
        send_text_message(reply_token, "🍴" + get_recipe_name(self.currenturl) + "\n\n" + find_ingredient(self.currenturl))

    def on_enter_shownutrition(self, event):
        id = event.source.user_id

        imgs = ["https://fooduncut.com/wp-content/uploads/2021/08/Chinese-Cooking-Hacks.jpg",
            "https://esmmweighless.com/wp-content/uploads/2019/12/Carolyn-Cooking-Blog.jpg",
            "https://goodfoodireland.ie/wp-content/uploads/2021/04/copy-of-copy-of-untitled-1.jpg"
        ]
        titles = ["Navigation Menu", "Navigation Menu", "Navigation Menu"]
        titletexts = ["Navigate to the recipe menu", "Navigate to the cooking method", "Navigate to the ingredient list"]
        labels = ["Back to Recipes", "Look up Method", "Look up Ingredients"]
        texts = ["search recipes", "show method", "show ingredients"]

        n_imgs = ["https://i.pinimg.com/564x/19/db/c1/19dbc114df24bb75fe1d1692fc3b5418.jpg",
            "https://c4.wallpaperflare.com/wallpaper/771/184/50/spongebob-squarepants-wallpaper-preview.jpg",
            "https://i.pinimg.com/564x/32/0d/c2/320dc2e12cd1c45cd9d6dd50464ee4f9.jpg",
            "https://i.pinimg.com/564x/e6/7f/25/e67f2518d5c517c93890eacd0964daf5.jpg",
            "https://pbs.twimg.com/media/D6ymCLrXsAIjspC?format=jpg&name=small",
            "https://i.pinimg.com/564x/db/a1/66/dba1667ede306ca32c0b2fdf303d2346.jpg",
            "https://www.shitpostbot.com/img/sourceimages/fiber-57de2d2707550.jpeg",
            "https://i.pinimg.com/564x/3d/6b/e4/3d6be4592e7acae3e4c6796954a0df0b.jpg",
            "https://www.wateraid.org/uk/sites/g/files/jkxoof211/files/styles/full_grid_image_2x/public/spongebob-dried-out-in-a-particularly-water-scarce-moment.jpg?itok=DWFZowSP",
        ]
        n_titles = ["NUTRITION FACTS", "KCAL", "FAT", "SATURATES", "CARBS", "SUGARS", "FIBRE", "PROTEIN", "SALT"]
        n_titletexts = ["🍴" + get_recipe_name(self.currenturl)]
        n_titletexts += find_nutrition(self.currenturl)
        n_labels = ["Learn More", "Learn More", "Learn More", "Learn More", "Learn More", "Learn More", "Learn More", "Learn More", "Learn More"] 
        n_uris = [self.currenturl,
            "https://www.medicalnewstoday.com/articles/263028",
            "https://www.medicalnewstoday.com/articles/141442",
            "https://www.medicalnewstoday.com/articles/321655",
            "https://www.medicalnewstoday.com/articles/161547#:~:text=Carbohydrates%20are%20the%20main%20source,mainly%20found%20in%20plant%20foods.",
            "https://www.medicalnewstoday.com/articles/does-your-body-need-sugar",
            "https://www.medicalnewstoday.com/articles/146935#:~:text=Dietary%20fiber%2C%20also%20known%20as,%2C%20whole%20grains%2C%20and%20legumes.",
            "https://www.medicalnewstoday.com/articles/196279",
            "https://www.medicalnewstoday.com/articles/146677#sources"
        ]

        send_msg_carousel(id, imgs, titles, titletexts, labels, texts)
        send_uri_carousel(id, n_imgs, n_titles, n_titletexts, n_labels, n_uris)

    def on_enter_searchotherrecipe(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "What recipe are you searching for?\nType \"home\" to cancel search")

    def on_enter_showother(self, event):
        id = event.source.user_id
        reply_token = event.reply_token
        url = "https://www.bbcgoodfood.com/search/recipes?q=" + event.message.text

        recipeurls = find_urls(url)

        imgs = []
        titles = []
        titletexts = []
        labels = ["Cooking Method", "Ingredients", "Nutrition"]
        texts = ["show method", "show ingredients", "show nutrition"]
        datalist = []

        if len(recipeurls) == 0:
            send_text_message(reply_token, "No results for " + event.message.text)
        elif len(recipeurls) <= 4:
            send_text_message(reply_token, "Searching for " + event.message.text + "...")
            for i, recipeurl in enumerate(recipeurls):
                imgs.append(get_img_url(recipeurl))
                titles.append("Result #" + str(i+1))
                titletexts.append(get_recipe_name(recipeurl))
                datalist.append(recipeurl)
        else:
            send_text_message(reply_token, "Searching for " + event.message.text + "...")
            for i in range(4):
                imgs.append(get_img_url(recipeurls[i]))
                titles.append("Result #" + str(i+1))
                titletexts.append(get_recipe_name(recipeurls[i]))
                datalist.append(recipeurls[i])

        send_showrecipe_carousel(id, imgs, titles, titletexts, labels, texts, datalist)