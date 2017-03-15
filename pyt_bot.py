from flask import Flask
from flask import render_template, request
import logging
import telegram
import os
from urllib import parse

HOST = "https://bot.pyzl.com"
app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

global bot
bot = telegram.Bot(token='TOKEN')
botName = "@Pyzl_bot"

@app.route("/", methods=["POST", "GET"])
def setWebhook():
    if request.method == "GET":
        logging.info("Hello, Telegram!")
        return "OK, Telegram Bot!"

@app.route("/set_webhook_mathmode", methods=['GET'])
def setWebHookMathMode():
    s = bot.setWebhook("{}/mathmode".format(HOST))
    if s:
        return "{} WebHook Setup OK!".format(botName)
    else:
        return "{} WebHook Setup Failed!".format(botName)

@app.route("/mathmode", methods=["POST"])
def mathmode():
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True))
        if update is None:
            return "Show me your TOKEN please!"
        logging.info("Calling {}".format(update.message))
        handdle_message(update.message)
        return "ok"

# MathMode
def handdle_message(msg):
    text = msg.text
    if "/start" in text:
        bot.sendDocument(chat_id=msg.chat.id, document="BQADBQADBQADPAsZA1QWNplWJQ03Ag")
        helpInfo(msg)
    elif "/echo" in text:
        bot.sendDocument(chat_id=msg.chat.id, document="BQADBQADBQADPAsZA1QWNplWJQ03Ag")
    elif "/greek" in text:
        bot.sendDocument(chat_id=msg.chat.id, document='AgADBQADv6cxGzwLGQNcPYQn0TV48JzvvTIABG-YPC7ADExKZ3oBAAEC')
    elif "/emoji" in text:
        query = parseCommand(text) or [""]
        results = os.popen("emoji-query {}".format(query[0]), mode='r')
        sendTxtMsg(msg, "".join(results))
    elif "/tex" in text or "/latex" in text:
        query = parseCommand(text) or ["\Psi"]
        latex = parse.quote(" ".join(query))
        bot.sendPhoto(chat_id=msg.chat.id, photo="http://latex.codecogs.com/gif.latex?%5Chuge%20{}".format(latex))
    elif "/help" in text:
        helpInfo(msg)
    else:
        helpInfo(msg)

def helpInfo(msg):
    text ="""
/echo  - 嘿嘿嘿
/emoji - emoji-query Command
/greek - Return LaTex Greek Letters
/tex   - Convert LaTex to Image
/help  - Help Info
"""
    sendTxtMsg(msg, text)

def sendTxtMsg(msg, text):
    bot.sendMessage(chat_id=msg.chat.id, text=text)

def parseCommand(command):
    params = command.split(" ")
    if len(params) == 1:
        return None
    return params[1:]

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
