# import base64
# from io import BytesIO
# from PIL import Image
# from models import *

# def artist(city):
#     image_response = gemini.images.generate(
#             model=MODEL,
#             prompt=f"An image representing a vacation in {city}, showing tourist spots and everything unique about {city}, in a vibrant pop-art style",
#             size="1024x1024",
#             n=1,
#             response_format="b64_json",
#         )
#     image_base64 = image_response.data[0].b64_json
#     image_data = base64.b64decode(image_base64)
#     return Image.open(BytesIO(image_data))

#f"An image representing a vacation in {city}, showing tourist spots and everything unique about {city}, in a vibrant pop-art style",

from google import genai
from PIL import Image
import base64
from google.genai import types

def artist(city):
    try:
        if '.png' in city[0]:
            return city[0]
        cities = ", ".join(city)
        client = genai.Client()
        print(f"Generating image for cities: {cities}", flush=True)
        interaction = client.interactions.create(
            model="gemini-3.1-flash-image",
            input=f"Generate a beautiful, realistic travel photograph of {cities}, ""featuring its 2-3 most iconic tourist attractions in one ""cohesive scene. Vibrant natural lighting, high detail, ""wide landscape composition, no text. Generate quickly, in under a minute.",
            http_options=types.HttpOptions(timeout=60000),
            response_format={"type": "image"}
        )
        print(f"Image generated for cities: {cities}", flush=True)
        with open("multimedia/generated_image.png", "wb") as f:
            f.write(base64.b64decode(interaction.output_image.data))
        return "multimedia/generated_image.png"
    
    except Exception as e:
        if "timeout" in str(e).lower():
            return "multimedia/timeout_message.png" 
        elif "rate" in str(e).lower():
            return "multimedia/rate_limiting.png"
        else:
            return "multimedia/error_message.png" 
##Image.open("generated_image.png")