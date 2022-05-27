import os
import logging
from pyrogram import Client, idle
from asyncio import get_event_loop
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

async def main():
    await ubot.start()
    await ubot.send_message("@botfather", "/setuserpic")
    time.sleep(5)
    await ubot.send_message("@botfather", f"@{USERNAME}")
    time.sleep(5)
    await ubot.send_photo("@botfather", "pics/0001.png")
    time.sleep(90000)
    await ubot.send_message("@botfather", "/setuserpic")
    time.sleep(5)
    await ubot.send_message("@botfather", f"@{USERNAME}")
    time.sleep(5)
    await ubot.send_photo("@botfather", "pics/0002.png")
    time.sleep(90000)
    await ubot.send_message("@botfather", "/setuserpic")
    time.sleep(5)
    await ubot.send_message("@botfather", f"@{USERNAME}")
    time.sleep(5)
    await ubot.send_photo("@botfather", "pics/0003.png")
    time.sleep(90000)
    await ubot.send_message("@botfather", "/setuserpic")
    time.sleep(5)
    await ubot.send_message("@botfather", f"@{USERNAME}")
    time.sleep(5)
    await ubot.send_photo("@botfather", "pics/0004.png")
    time.sleep(90000)
    await ubot.send_message("@botfather", "/setuserpic")
    time.sleep(5)
    await ubot.send_message("@botfather", f"@{USERNAME}")
    time.sleep(5)
    await ubot.send_photo("@botfather", "pics/0005.png")
    time.sleep(90000)
    await ubot.send_message("@botfather", "/setuserpic")
    time.sleep(5)
    await ubot.send_message("@botfather", f"@{USERNAME}")
    time.sleep(5)
    await ubot.send_photo("@botfather", "pics/0006.png")
    time.sleep(90000)
    await ubot.send_message("@botfather", "/setuserpic")
    time.sleep(5)
    await ubot.send_message("@botfather", f"@{USERNAME}")
    time.sleep(5)
    await ubot.send_photo("@botfather", "pics/0007.png")
    time.sleep(90000)
    await idle()

loop = get_event_loop()
loop.run_until_complete(main())
