from openai import OpenAI
from config import openai_key
import requests

class Dall_E():
    def __init__(self):
        self.client = OpenAI(api_key=openai_key)

    def prompt_to_image(self, prompt):
        try:
            response = self.client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
            )
            image_url = response.data[0].url
            return image_url
        except requests.exceptions.RequestException as e:
            return f"{response.text}"