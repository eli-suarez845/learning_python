import requests
from send_email import send_email

topic = "tesla"
# core part
# parameters: q, sortBy, apiKey => Documentation-Endpoints-Everything
api_key = "ccc53e452e03443c9c06c9cb6a128200"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-08-13&sortBy=publishedAt&apiKey=ccc53e452e03443c9c06c9cb6a128200"

# Make a request
request = requests.get(url)

# Get a dicc with data
content = request.json()

# Access the article titles and description
body = ""

for article in content["articles"]:
    if article["title"] is not None:
        body = "Subject: Today's news" + "\n" + article["title"] + 2 * "\n" \
               + article["description"] + "\n" + article["url"]  # now you see the value of the articles key

body = body.encode("utf-8")
send_email(message=body)  # por alguna razón sólo me envía un artículo por mail
