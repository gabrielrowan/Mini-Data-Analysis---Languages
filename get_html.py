import requests
# Retrieves html from wikipedia page on top languages spoken stats

url = 'https://en.wikipedia.org/wiki/List_of_languages_by_number_of_native_speakers'

response = requests.get(url)
html = response.text

with open("languages_html.txt", "w", encoding="utf-8") as file:
    file.write(html)
