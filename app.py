import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from linebot.models.events import PostbackEvent
from linebot.webhook import WebhookHandler

from fsm import TocMachine
from utils import send_text_message

load_dotenv()

machine = TocMachine()

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
        if isinstance(event, PostbackEvent):
            response = machine.advance(event)
        else:
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
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if isinstance(event, PostbackEvent):
            response = machine.advance(event)
        else:
            response = machine.advance(event)

            if response == False:                  
                if event.message.text.lower() == 'home':
                    machine.go_back(event)
                else:
                    send_text_message(event.reply_token, "Error, invalid command try again!")

    return "OK"

if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
