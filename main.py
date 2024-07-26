import requests
from dotenv import load_dotenv
import os

load_dotenv()

STABILITY_API_KEY = os.getenv("STABILITY_API_KEY")

response = requests.post(
    f"https://api.stability.ai/v2beta/stable-image/generate/sd3",
    headers={
        "authorization": STABILITY_API_KEY,
        "accept": "image/*"
    },
    files={"none": ''},
    data={
        "prompt": "masterpiece, best quality, 1girl, blonde hair, wearing camisole, BREAK beautiful eyes, clear dark eyes, detailed eyes, eyes <lora:eyes:1>",
        "negative_prompt": "bad-picture-chill-75v, badpic",
        "output_format": "jpeg",
    },
)

if response.status_code == 200:
    with open("./1girl.jpeg", 'wb') as file:
        file.write(response.content)
else:
    raise Exception(str(response.json()))
