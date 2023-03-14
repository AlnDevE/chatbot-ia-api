
import random
from tkinter import *
from datas import objectives, model, lemmatizer, words, classes
import nltk
import numpy as np

def get(message: str):
    ints = predict_class(message)
    return get_response(ints, objectives)
    
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(
        word.lower()) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence, words, show_details=True):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, word in enumerate(words):
            if word == s:
                bag[i] = 1
                if show_details:
                    print("found in bag of data: %s" % word)
    return (np.array(bag))


def predict_class(sentence):
    p = bag_of_words(sentence, words, show_details=True)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"objective": classes[r[0]], "probability": str(r[1])})
    return return_list


def get_response(ints, objectives_json):
    tag = ints[0]['objective']
    list_of_objectives = objectives_json['objectives']
    for i in list_of_objectives:
        if (i['tag'] == tag):
            result = random.choice(i['responses'])
            break
    return result