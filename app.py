import requests
from pprint import pprint
import json


response = requests.get('https://suggestqueries.google.com/complete/search?client=chrome&hl=en&gl=us&callback=__ng_jsonp__.__req3.finished&q=python%20library')

dataForJSON = response.content.decode("utf-8").split("(", 1)[1].strip(")")
currentJson = json.loads(dataForJSON)

print(currentJson[0], '------->' , currentJson[1])
