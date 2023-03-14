import json
import pickle
from tkinter import *
from keras.models import load_model
from nltk.stem import WordNetLemmatizer
from train import train_ia

try:
    lemmatizer = WordNetLemmatizer()
    model = load_model('chat_fatec_model.h5')
    objectives = json.loads(open('objectives.json').read())
    words = pickle.load(open('all_words.pkl', 'rb'))
    classes = pickle.load(open('all_classes.pkl', 'rb'))
except:
    train_ia()