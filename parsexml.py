from __future__ import division
from bs4 import BeautifulSoup
import os
from rake_tutorial import extractWords
import io
import ntpath


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



for root, dirs, files in os.walk("/home/kjani/Desktop/LexisNexis/test_data", topdown=False):
    for name in files:
        # print(os.path.join(root, name))
        extractContent(os.path.join(root, name))

# for key, value in catchPhrasesDict.iteritems():
#     print key
#     print value


summary_word_lengths = min_char_lens = max_word_lengths = min_frqs = range(5, 0, -1)
print summary_word_lengths

# max_value = 0
# key = "dataset_training/06_11.xml"
# value = sentencesFromSource[key]
#
# for min_char_len in min_char_lens:
#     for max_word_length in max_word_lengths:
#         for min_frq in min_frqs:
#             for summary_word_length in summary_word_lengths:
#                 extracted_words = extractWords(value[0], min_char_len, max_word_length, min_frq, len(value[0])*summary_word_length/10)
#                 extracted_word_list = []
#                 [extracted_word_list.append(x[0].split()) for x in extracted_words]
#                 extracted_word_list = set([item for sublist in extracted_word_list for item in sublist])
#
#                 training_keywords = [x.split() for x in catchPhrasesDict[key]]
#                 training_keywords = set([item for sublist in training_keywords for item in sublist])
#
#                 subtracted_list = training_keywords - extracted_word_list
#                 matching = len(training_keywords) - len(subtracted_list)
#                 print matching
#                 result = (matching/len(training_keywords))
#                 print result
#                 print min_char_len, max_word_length, min_frq, summary_word_length
#                 if(result > max_value):
#                     max_value = result
#                 # print len(training_keywords)
#                 print '------------------------------------------------'
#
# print max_value



## For training the model
# for key, value in sentencesFromSource.iteritems():
#     print(os.path.basename(key))
#     extracted_words, summary = extractWords(value[0], 5, 3, 4, len(value[0])*0.01)
#     extracted_word_list = []
#     [extracted_word_list.append(x[0]) for x in extracted_words]
#     extracted_word_list = set([item for sublist in extracted_word_list for item in sublist])
  


#     training_keywords = [x.split() for x in catchPhrasesDict[key]]
#     training_keywords = set([item for sublist in training_keywords for item in sublist])

#     subtracted_list = training_keywords - extracted_word_list
#     matching = len(training_keywords) - len(subtracted_list)
#     print (matching/len(training_keywords))
#     # print len(training_keywords)
#     print '------------------------------------------------'

for key, value in sentencesFromSource.iteritems():
    print("~~~~ processing file:  "+os.path.basename(key)+"  ~~~~")
    extracted_words, summary = extractWords(value[0], 5, 3, 4, len(value[0])*0.01)
    extracted_word_list = []
    [extracted_word_list.append(x[0]) for x in extracted_words]
    # extracted_word_list = set([item for sublist in extracted_word_list for item in sublist])

    keyphraseFile = io.open('/home/kjani/Desktop/LexisNexis/catchPhrases/' + os.path.basename(key), 'w')
    
    keyphraseFile.write(u'CatchPhrases:'+"\n")
    for keyphrase in extracted_word_list:
        keyphraseFile.write(keyphrase + "\n")
    keyphraseFile.write(u'==============================================================================================================='+"\n")
    keyphraseFile.write(u'Summary:'+"\n")
    keyphraseFile.write(summary + "\n")
    keyphraseFile.close()


    # training_keywords = [x.split() for x in catchPhrasesDict[key]]
    # training_keywords = set([item for sublist in training_keywords for item in sublist])

    # subtracted_list = training_keywords - extracted_word_list
    # matching = len(training_keywords) - len(subtracted_list)
    # print (matching/len(training_keywords))
    # # print len(training_keywords)
    # print '------------------------------------------------'





