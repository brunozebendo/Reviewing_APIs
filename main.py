"""a intenção do código é criar uma API para pegar uma imagem
e um texto do site do NASA, para isso foi usada a sintaxe abaixo que já expliquei
bastante no outro curso, valendo ressaltar apenas o streamlit que é
usado para facilitar a escrita no PYTHON, abaixo, ele gerou uma sequência
de título, imagem e texto, sem precisar de muito mais informação"""
import requests
import streamlit as st

# Prepare API key and API url
api_key = "Ngt6d9k6dY2f3BZRDdpgGzgClzjiwsFbQ42Aqfnv"
url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}"

# Get the request data as a dictionary
response1 = requests.get(url)
data = response1.json()

# Extract the image title, url and, explanation
title = data["title"]
image_url = data["url"]
explanation = data["explanation"]

# Download the image
image_filepath = "img.png"
response2 = requests.get(image_url)
with open(image_filepath, 'wb') as file:
    file.write(response2.content)

st.title(title)
st.image(image_filepath)
st.write(explanation)
