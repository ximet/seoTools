import requests
import urllib.parse
import json

def sizeDescription(text):
    countLetters = len(text)
    error = []
    if countLetters == 0:
        error.append("You have not added a meta description. As a result, you will get access to your page.")
    if countLetters < 150:
        error.append("To small a meta description. Please, write more...")
    if countLetters > 160:
        error.append("You have to much information in a meta description")
    return countLetters, text, error