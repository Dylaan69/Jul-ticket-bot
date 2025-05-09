from keep_alive import keep_alive
import requests
from bs4 import BeautifulSoup
import time

# >>> CONFIG <<<
BOT_TOKEN = "7572591928:AAHwEM2lT4IUQBRoOH2rQkz4ry0fUzg0Uik"
TELEGRAM_CHAT_ID = "247319776"
CHECK_INTERVAL = 60  # toutes les 60 secondes

URLS = [
    "https://www.ticketmaster.fr/fr/manifestation/jul-billet/idmanif/581329",
    "https://www.ticketmaster.fr/fr/manifestation/jul-billet/idmanif/618685"
]

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(url, data=payload)

def check_ticket():
    headers = {"User-Agent": "Mozilla/5.0"}
    for url in URLS:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        if "revente" in soup.text.lower() or "acheter" in soup.text.lower():
            send_telegram_message(f"🎫 **Des billets sont dispos pour JUL !**\n{url}")
            return True
    print("Pas de billets pour le moment...")
    return False

keep_alive()

while True:
    try:
        dispo = check_ticket()
        if dispo:
            time.sleep(300)  # attend 5 minutes si billets trouvés
        else:
            time.sleep(CHECK_INTERVAL)
    except Exception as e:
        print("Erreur :", e)
        time.sleep(60)


