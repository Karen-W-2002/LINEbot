import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from linebot.models.events import PostbackEvent

from fsm import TocMachine
from utils import send_text_message

load_dotenv()


machine = TocMachine(
    states=["user", "start", "searchrecipe", "searchchef",
            "showbreakfast", "showlunch", "showdinner", "showchefrecipes",
            "showmethod", "showingredient", "shownutrition",
            "searchotherrecipe", "showother"],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "start",
            "conditions": "is_going_to_start"
        },
       {
            "trigger": "advance",
            "source": ["start", "showbreakfast", "showlunch", "showdinner", "showchefrecipes", "showmethod", "showingredient", "shownutrition", "showother"],
            "dest": "searchrecipe",
            "conditions": "is_going_to_searchrecipe"
        },
        {
            "trigger": "advance",
            "source": ["start", "searchrecipe", "showother", "showbreakfast", "showlunch", "showdinner", "showchefrecipes"],
            "dest": "searchotherrecipe",
            "conditions": "is_going_to_searchotherrecipe"
        },
        {
            "trigger": "advance",
            "source": ["start", "showchefrecipes"],
            "dest": "searchchef",
            "conditions": "is_going_to_searchchef"
        },
        {
            "trigger": "advance",
            "source": "searchrecipe",
            "dest": "showbreakfast",
            "conditions":"is_going_to_showbreakfast"
        },
        {
            "trigger": "advance",
            "source": "searchrecipe",
            "dest": "showlunch",
            "conditions":"is_going_to_showlunch"
        },
        {
            "trigger": "advance",
            "source": "searchrecipe",
            "dest": "showdinner",
            "conditions":"is_going_to_showdinner"
        },
        {
            "trigger": "advance",
            "source": ["searchchef", "searchrecipe"],
            "dest": "showchefrecipes",
            "conditions": "is_going_to_showchefrecipes"
        },
        {
            "trigger": "advance",
            "source": ["showbreakfast", "showlunch", "showdinner", "showchefrecipes", "showingredient", "shownutrition", "showother"],
            "dest": "showmethod",
            "conditions": "is_going_to_showmethod"
        },
        {
            "trigger": "advance",
            "source": ["showbreakfast", "showlunch", "showdinner", "showchefrecipes", "showmethod", "shownutrition", "showother"],
            "dest": "showingredient",
            "conditions": "is_going_to_showingredient"
        },
        {
            "trigger": "advance",
            "source": ["showbreakfast", "showlunch", "showdinner", "showchefrecipes", "showmethod", "showingredient", "showother"],
            "dest": "shownutrition",
            "conditions": "is_going_to_shownutrition"
        },
        {
            "trigger": "advance",
            "source": "searchotherrecipe",
            "dest": "showother",
            "conditions": "is_going_to_showother"
        },
        {"trigger": "go_back", "source": ["searchrecipe", "searchotherrecipe", "searchchef", "showother", 
        "showbreakfast", "showlunch", "showdinner", "showchefrecipes"], "dest": "start"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)
#current_url = ""


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue

        response = machine.advance(event)

        if response == False:                  
            if event.message.text.lower() == 'home':
                machine.go_back(event)
            else:
                send_text_message(event.reply_token, "Error, invalid command try again!")

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "Not Entering any State")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
