from __future__ import absolute_import
from __future__ import print_function
import six

__author__ = 'a_medelyan'

import textrank
import rake
import operator
import re
from summa import summarizer

# EXAMPLE ONE - SIMPLE
stoppath = "SmartStoplist.txt"

keyword_shortlist_length = 3


def extractWords(sentence, min_char_len, max_word_length, min_frq, summary_word_length):
    # 1. initialize RAKE by providing a path to a stopwords file
    rake_object = rake.Rake(stoppath, min_char_len, max_word_length, min_frq)

    # # 2. run on RAKE on a given text
    # sample_file = io.open("data/docs/fao_test/06_450.xml", 'r',encoding="iso-8859-1")
    # text = sample_file.read()

    keywords = rake_object.run(sentence)

    summary = summarizer.summarize(sentence, words=summary_word_length)

    #summary2 = textrank.extractSentences(sentence)

    #print(summary)
    print("~~~~ generating Catchphrases ~~~~")
    print("~~~~ generating Summary ~~~~")
    print("############################################")
    #print(summary2)

    # return keywords

    # # 3. print results
    # # keywords.sort(key=lambda x: x[1])
    # # print("Keywords:", keywords)
    #
    # print("----------")
    # # EXAMPLE TWO - BEHIND THE SCENES (from https://github.com/aneesha/RAKE/rake.py)
    #
    # # 1. initialize RAKE by providing a path to a stopwords file
    rake_object = rake.Rake(stoppath)
    #
    # # text = "Compatibility of systems of linear constraints over the set of natural numbers. Criteria of compatibility " \
    # #      "of a system of linear Diophantine equations, strict inequations, and nonstrict inequations are considered. " \
    # #       "Upper bounds for components of a minimal set of solutions and algorithms of construction of minimal generating"\
    # #       " sets of solutions for all types of systems are given. These criteria and the corresponding algorithms " \
    # #       "for constructing a minimal supporting set of solutions can be used in solving all the considered types of " \
    # #       "systems and systems of mixed types."
    #
    #
    #
    # # 1. Split text into sentences
    sentenceList = rake.split_sentences(sentence)
    sentenceList = [re.sub("\s\s+", " ", sentence) for sentence in sentenceList]
    # sentenceList = list(filter(None, sentenceList))
    # print("=========================================================================================")
    # print("=========================================================================================")
    # print("=========================================================================================")
    # for sentence in sentenceList:
    #     sentense = re.sub("\s\s+", " ", sentence)
    # for sentence in sentenceList:
    #     print("Sentence:", sentence)
    # print("=========================================================================================")
    # print("=========================================================================================")
    # print("=========================================================================================")
    # # generate candidate keywords
    stopwordpattern = rake.build_stop_word_regex(stoppath)
    phraseList = rake.generate_candidate_keywords(sentenceList, stopwordpattern)
    # # print("Phrases:", phraseList)
    #
    # # calculate individual word scores
    wordscores = rake.calculate_word_scores(phraseList)
    #
    # # generate candidate keyword scores
    keywordcandidates = rake.generate_candidate_keyword_scores(phraseList, wordscores)
    # # for candidate in keywordcandidates.keys():
    # #    print("Candidate: ", candidate, ", score: ", keywordcandidates.get(candidate))
    #
    # # sort candidates by score to determine top-scoring keywords

    max_key = (max(keywordcandidates, key=keywordcandidates.get))
    max_value = (keywordcandidates[max_key])

    for key, value in keywordcandidates.iteritems():
        if(key in summary):
            keywordcandidates[key] = value + max_value



    sortedKeywords = sorted(six.iteritems(keywordcandidates), key=operator.itemgetter(1), reverse=True)
    totalKeywords = len(sortedKeywords)
    sortedKeywords = sortedKeywords[:15]

    return sortedKeywords, summary
    #
    # for example, you could just take the top third as the final keywords
    # for keyword in sortedKeywords[0:int(totalKeywords / keyword_shortlist_length)]:
    #     print("Keyword: ", keyword[0], ", score: ", keyword[1])



