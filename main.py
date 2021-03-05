# For this week, you're going to be working on a mashup! 
# You'll use the code to scrape a random fact from http://unkno.com 
# (Links to an external site.)Links to an external site. 
# that we developed in class, and send it to a 
# pig latin web application running on Heroku. 
# The address of the Pig Latinizer is: 
# https://hidden-journey-62459.herokuapp.com/ (Links to an external site.)Links to an external site. 
#
# The requirement is:
#
#    You should deploy your assignment to Heroku.
#    Whenever someone visits your home page, it should 
# scrape a new fact from unkno.com, send that fact to the 
# pig latin website, and print out the address for that piglatinized fact on the home page.

import os

import requests
from flask import Flask
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()

def get_piglatin_url(text: str):
    payload={'input_text' : text}
    x = requests.post('https://hidden-journey-62459.herokuapp.com/piglatinize/', data=payload)
    return x.url
 

@app.route('/')
def home():
    sFact = get_fact()
    url = get_piglatin_url(sFact)
    print(sFact, url)
    return f'<a href={url}>{url}</a>'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

