import requests
import time

BOT_TOKEN = "APNA_TOKEN_YAHAN"
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

def get_updates(offset=None):
    return requests.get(BASE_URL + "/getUpdates", params={"timeout": 100, "offset": offset}).json()

def send_message(chat_id, text):
    requests.get(BASE_URL + "/sendMessage", params={"chat_id": chat_id, "text": text})

offset = None

while True:
    data = get_updates(offset)

    for update in data.get("result", []):
        offset = update["update_id"] + 1

        if "message" in update:
            chat_id = update["message"]["chat"]["id"]
            text = update["message"].get("text", "")

            if text == "/start":
                send_message(chat_id, "🔥 Bot 24/7 online hai!")
            else:
                send_message(chat_id, "Reply mil gaya ✅")

    time.sleep(2)
