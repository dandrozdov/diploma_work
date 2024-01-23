import requests
from src.config import URL, TOKEN, CHAT_ID, TELEGRAM_LIMIT


def send_msg_to_telegram(text):
    split_message = (text[position:position + TELEGRAM_LIMIT] for position in range(0, len(text), TELEGRAM_LIMIT))

    for message in split_message:
        url_req = f'{URL}{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}'
        requests.get(url_req)
