"""import requests

url = "https://hips.hearstapps.com/hmg-prod/images/russian-blue-royalty-free-image-1658451809.jpg"

response = requests.get(url)
print(response)  # => <Response [200]> 200 is an HTTP code which means response was successful

print(response.content)
with open("first_image.jpg", "wb") as file:
    file.write(response.content)"""

import streamlit as st  # install st in Py packages
import pandas as pd
import requests

# Prepare API key and API url
api_key = "w6ADD4czEj8nENmB8PPuY4pAmPN7IyizZLsCtt4F"
url = "https://api.nasa.gov/planetary/apod?api_key=w6ADD4czEj8nENmB8PPuY4pAmPN7IyizZLsCtt4F"

# Get request as dictionary
response1 = requests.get(url)
data = response1.json()

# Extract image title, url & explanation
title = data["title"]
image_url = data["url"]
explanation = data["explanation"]

# Download image
image_filepath = "image.png"
response2 = requests.get(image_url)
with open(image_filepath, "wb") as file:
    file.write(response2.content)

st.title(title)
st.image(image_filepath)
st.write(explanation)
