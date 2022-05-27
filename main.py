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
SESSION = """
BQBqhj3fo3i-p7L15h0py0Mo31-L43YgddSYldhiJjowPOQWJqceeDfqMydJmK1FXUPdz1VxUxArlZHcH5VeT_PHTuNehZXUKi_TSXCZFQSzBNDokPrRYsJibl9ioXo78gxS8Lvu4GnLuRCQlAmpVS0oQ3UVfZVgibVCKiRlw554l_BCWqn7mAFRD7KROJBJFFjTzSUpx0xo2Uu47xxXwHmjr711k15nhmEW1UQzI8uhNlcrMCgaLZEj8f2QJJQqf-cb9TjGsT5SzokTmh2d-nSuHPNioGoPNkHMhhnUl9s2SqPaIg7rPmCmnNizDs0-ZNsU1gCWCgh3WLO_bsTB5KGNAAAAAT1MlXEA
"""
USERNAME = os.environ.get("USERNAME", None) 

# For Local Deploy:
"""
API_ID = ""
API_HASH = ""
SESSION = ""
USERNAME = ""
"""

ubot = Client(
      name=SESSION,
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
    
