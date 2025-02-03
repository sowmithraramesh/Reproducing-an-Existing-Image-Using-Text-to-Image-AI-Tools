This code uses OpenAI's DALL-E API to generate an image based on a crafted prompt.
import openai
from PIL import Image
import requests
from io import BytesIO
# OpenAI API Key
openai.api_key = "your_openai_api_key"
# Function to generate image using DALL-E
def generate_image(prompt):
response = openai.Image.create(
prompt=prompt,
n=1,
size="1024x1024"
)
image_url = response['data'][0]['url']
return image_url
# Analyzing the image and crafting a prompt
# Example Image Description:
# "A calm beach scene during sunset with a clear sky, golden sun, waves gently crashing, and a
silhouette of a lone person standing on the shore."
# Generating Image
prompt = "A calm beach scene during sunset with a clear sky, golden sun, waves gently crashing, and
a silhouette of a lone person standing on the shore."
image_url = generate_image(prompt)
# Displaying the generated image
response = requests.get(image_url)
img = Image.open(BytesIO(response.content))
img.show()
print("Generated Image URL:", image_url)
