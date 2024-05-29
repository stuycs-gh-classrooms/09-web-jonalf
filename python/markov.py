#!/usr/bin/python
print('Content-type: text/html\n')

from random import choice, random
from pprint import pprint

f = open('data/holmes.txt', encoding='utf-8')
scripts = f.read()

def make_markov_model1(s):
    l = s.split()
    d = {}
    w = 0
    while (w < len(l)-2):
        if l[w] + ' ' + l[w+1] in d:
            if l[w+2] in d[l[w] + ' ' + l[w+1]]:
                d[l[w] + ' ' + l[w+1]][l[w+2]]+= 1
            else:
                d[l[w] + ' ' + l[w+1]][l[w+2]] = 1
        else:
            d[l[w] + ' ' + l[w+1]] = {l[w+2]: 1}
        w+=1
    #print(d)
    for key in d:
        total_words = sum(d[key].values())
        for word in d[key]:
            d[key][word] = d[key][word]/total_words

    return d


def make_markov_model(s):
    words = s.split()
    d = {}
    w = 0
    while (w < len(words)-2):
        token = words[w:w+3]
        key = ' '.join(token[:2])
        next_word = token[2]
        if key in d:
            if next_word in d[key]:
                d[key][next_word]+= 1
            else:
                d[key][next_word] = 1
        else:
            d[key] = {next_word: 1}
        w+=1
    #print(d)
    for key in d:
        total_words = sum(d[key].values())
        for word in d[key]:
            d[key][word] = d[key][word]/total_words

    return d

def get_next_word(model, key):
    odds = model[key]
    r = random()
    total = 0
    for word in odds:
        total+= odds[word]
        if r < total:
            return word

def generate_text(model, num_words):
    text = []
    key = choice(list(model.keys()))
    text+= key.split(' ')
    i = 0
    while i < num_words:
        next_word = get_next_word(model, key)
        text.append(next_word)
        key = key.split(' ')
        key = key[1] + ' ' + next_word
        i+= 1
    return ' '.join(text)


model = make_markov_model(scripts)
key = choice(list(model.keys()))
print(generate_text(model, 100))
