from bs4 import BeautifulSoup
import os
from rake_tutorial import extractWords

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

# for key, value in catchPhrasesDict.iteritems():
#     print key
#     print value

for key, value in sentencesFromSource.iteritems():
    extracted_words = extractWords(value[0], 5, 3, 4, len(value[0])*0.1)
    extracted_words = [x[0] for x in extracted_words]
    print extracted_words
    print catchPhrasesDict[key]
    print "-----------------------------------------------------------"
    break



