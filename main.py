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
BQDBFePXlgEzIB6b5e1WPvEQFAqK4FLN1b4pr6C0hPM08dZb9QNXcC03aIVO_uUwy7nnw64eBD6NYpvsIM6OUirApKN9DuLbbJUJPmoj2mNi6aaXWq_ogExhR4U0t3a71p0ujz-_4TkccxSOUVEeoqAWVnPr8qANJD9s3S5izOwOHn3s1QXgNvudGx2pzWF9A2069NzKKltfhY3z9QsQWnDZFE0pGBDxUkSxvSJnlyqD2X645Vrbgjox7qm9_bA-t8cZejBeOKNt3NT4ZSWGb3K1skUmizPlNnS6_kDIn4FiSkCoYu-FM3cx6nt87_cMBXhJUoumaWUZAq5aQXI_ePh8AAAAAT1MlXEA 
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

ubot.run()

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
    
