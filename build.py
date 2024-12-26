import json
import csv

def load_words_from_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)

    words = {}

    for entry in data:
        word = entry['word']
        type = entry['type']
        definition = entry['definition']

        words[word] = WordCard(word, type, definition)

    return words

class WordCard:
    def __init__(self, word, type, definition, repetitions = 0, interval = 1, review_counter = 0, is_new = True):
        self.word = word
        self.type = type
        self.definition = definition
        self.repetitions = repetitions
        self.intervals = interval
        self.review_counter = review_counter
        self.is_new = is_new
    
    def update_word():
        return
    
    def is_learned():
        return
    
if __name__ == '__main__':
    word_cards = load_words_from_json('sat_words.json')
    print(word_cards)