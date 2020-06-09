
import requests
from bs4 import BeautifulSoup

# request then parse the contents of the website
response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")  # pass the html object and the type of parser as arguments
questions = soup.select(".question-summary")  # pass the CSS selector as an argument to return a list of tag objects

# Iterate over the tag objects, get the HTML object, convert it to text then print it
i = 1
for question in questions:
    print(str(i) + ". " + question.select_one(".question-hyperlink").getText())
    print("Votes: " + question.select_one(".vote-count-post").getText())
    i += 1
