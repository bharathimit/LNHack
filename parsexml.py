from bs4 import BeautifulSoup
import os

catchPhrasesDict = {}
sentencesFromSource = {}


def extractContent(filePath):
    catchPhrases = []
    sentences = []
    xmlText = open(filePath).read()
    xml = BeautifulSoup(xmlText, "html.parser")
    for tag in xml.findAll('catchphrase'):
        catchPhrases.append(tag.text)
    catchPhrasesDict[filePath] = catchPhrases

    for tag in xml.findAll('sentences'):
        sentences.append(tag.text)

    sentencesFromSource[filePath] = sentences



for root, dirs, files in os.walk("dataset_training", topdown=False):
    for name in files:
        # print(os.path.join(root, name))
        extractContent(os.path.join(root, name))

for key, value in catchPhrasesDict.iteritems():
    print key
    print value

for key, value in sentencesFromSource.iteritems():
    print key, value
