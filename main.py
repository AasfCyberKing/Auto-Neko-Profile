import os
import logging
from pyrogram import Client
import requests
import time

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

API_ID = os.environ.get("API_ID", None) 
API_HASH = os.environ.get("API_HASH", None) 
SESSION = os.environ.get("SESSION", None) 
USERNAME = os.environ.get("USERNAME", None) 

# For Local Deploy:
"""
API_ID = ""
API_HASH = ""
SESSION = ""
USERNAME = ""
"""

ubot = Client(
      session_name=SESSION,
      api_id=API_ID,
      api_hash=API_HASH,
)

while True:
    url = "https://nekos.best/api/v2/neko"
    r = requests.get(url)
    e = r.json()
    pics = e["results"][0]["url"]
    ubot.send_message("@botfather", "/setuserpic")
    time.sleep(5)
    ubot.send_message("@botfather", f"@{USERNAME}")
    times.sleep(5)
    ubot.send_photo("@botfather", pics)
    times.sleep(90000)
    ubot.send_message("@botfather", "/setuserpic")
    time.sleep(5)
    ubot.send_message("@botfather", f"@{USERNAME}")
    times.sleep(5)
    ubot.send_photo("@botfather", pics)
    times.sleep(90000)
    
