import requests
import urllib.parse
import json

API_URL = 'https://suggestqueries.google.com/complete/search?client=chrome&hl=en&gl=us&callback=__ng_jsonp__.__req3.finished&q='

print('Please, write your word: ')
inputText = urllib.parse.quote(input())

def getSuggestionFromSearchEngine(apiURL, inputString):
    response = requests.get(API_URL + inputText)

    dataForJSON = response.content.decode("utf-8").split("(", 1)[1].strip(")")
    currentJson = json.loads(dataForJSON)

    print(currentJson[0], '------->' , currentJson[1])

getSuggestionFromSearchEngine(API_URL, inputText)