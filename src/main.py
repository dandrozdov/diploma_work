from flask import Flask, request
from integrations.telegram import send_msg_to_telegram

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    send_msg_to_telegram(request.json['message'])
    return {'result': 'Message sended to Telegram.'}


if __name__ == "__main__":
    app.run()
