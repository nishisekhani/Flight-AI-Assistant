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


from google import genai
from PIL import Image
import base64

def artist(city):
    client = genai.Client()

    interaction = client.interactions.create(
        model="gemini-3.1-flash-image",
        input=f"An image representing a vacation in {city}, showing tourist spots and everything unique about {city}, in a vibrant pop-art style",
    )
    with open("generated_image.png", "wb") as f:
        f.write(base64.b64decode(interaction.output_image.data))

    return "generated_image.png"
##Image.open("generated_image.png")