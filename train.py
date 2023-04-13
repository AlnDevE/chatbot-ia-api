import pickle
import random
import nltk
import numpy as np
from keras.layers import Dense, Dropout
from keras.models import Sequential
from keras.optimizers import SGD
from nltk.stem import WordNetLemmatizer
from file import get_file
nltk.download('punkt')
nltk.download('wordnet')
import json

def train_ia():
    lemmatizer = WordNetLemmatizer()
    objectives = get_file()

    words = []
    classes = []
    documents = []
    ignore_letters = ['!', '?', ',', '.']

    for objective in objectives['objectives']:
        for patterns in objective['patterns']:
            word = nltk.word_tokenize(patterns)
            words.extend(word)
            documents.append((word, objective['tag']))
            if objective['tag'] not in classes:
                classes.append(objective['tag'])

    words = [lemmatizer.lemmatize(w.lower())
            for w in words if w not in ignore_letters]
    words = sorted(list(set(words)))
    classes = sorted(list(set(classes)))

    pickle.dump(words, open('all_words.pkl', 'wb'))
    pickle.dump(classes, open('all_classes.pkl', 'wb'))

    training = []
    output_empty = [0] * len(classes)
    for doc in documents:
        bag = []
        patterns_words = doc[0]
        patterns_words = [lemmatizer.lemmatize(
            word.lower()) for word in patterns_words]
        for word in words:
            bag.append(1) if word in patterns_words else bag.append(0)

        output_row = list(output_empty)
        output_row[classes.index(doc[1])] = 1

        training.append([bag, output_row])
        
    random.shuffle(training)
    training = np.array(training)
    train_x = list(training[:, 0])
    train_y = list(training[:, 1])

    model = Sequential()
    model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(len(train_y[0]), activation='softmax'))

    sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy',
                optimizer=sgd, metrics=['accuracy'])

    hist = model.fit(np.array(train_x), np.array(train_y),
                    epochs=200, batch_size=5, verbose=1)
    model.save('chat_fatec_model.h5', hist)
    
def get_trainings():
    trainings = json.loads(open('objectives.json').read())
    return trainings['objectives']