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
    def __init__(self, word, type, definition, repetitions = 0, interval = 1, ease_factor = 2, review_counter = 0, is_new = True):
        self.word = word
        self.type = type
        self.definition = definition
        self.repetitions = repetitions
        self.interval = interval
        self.ease_factor = ease_factor
        self.review_counter = review_counter
        self.is_new = is_new
    
    def update_word(self):
        if self.repetitions == 0:
            self.interval = 2
        elif self.repetitions == 1:
            self.interval = 4
        else:
            self.interval = round(self.interval * self.ease_factor)
        
        self.repetitions += 1
        self.is_new = False
        self.ease_factor = max(1.5, self.ease_factor + 0.1)
        self.review_counter = self.interval
    
    def is_learned(self, max_repetitions = 5):
        return self.repetitions >= max_repetitions
    
if __name__ == '__main__':
    word_cards = load_words_from_json('sat_words.json')
    print(word_cards['influence'].type)