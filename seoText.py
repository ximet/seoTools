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

def countWords(text):
    return len(text.split())

def getWordsFrequencies(text):
    wordList = text.split()
    wordFreq = [wordList.count(w) for w in wordList]

    return dict(list(zip(wordList, wordFreq)))

def getWordFrequancies(text, word):
    wordsFrequencies = getWordsFrequencies(text)
    if word in wordsFrequencies:
        return wordsFrequencies[word]
    else: 
        return 0

print(getWordFrequancies("ololo Hello world, ololo are you ready, ololo?", "item"))