import json
import csv

def load_words_from_json(path):
    with open(path, 'r') as f:
        data = json.load(f)

    dictionary = {}

    for word, definition in data.items():
        dictionary[word] = Card(word, definition)

    return dictionary

def write_words_to_csv(words, path):
    with open(path, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        for word in words:
            writer.writerow([word])

class Card:
    def __init__(self, word, definition, repetitions = 0, interval = 1, ease_factor = 2, review_counter = 0, is_new = True):
        self.word = word
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
        self.ease_factor = self.ease_factor + 0.1
        self.review_counter = self.interval
    
    def is_learned(self, max_repetitions = 5):
        return self.repetitions >= max_repetitions
    
def get_due_words(cards):
    due_words = []

    for card in cards.values():
        if card.review_counter <= 0 and not card.is_new:
            due_words.append(card)

    return due_words

def review_session(cards, max_repetitions = 5):
    history = []
    total_words_reviewed = 0

    while True:
        for card in cards.values():
            if card.review_counter > 0:
                card.review_counter -= 1

        due_words = get_due_words(cards)

        if not due_words:
            filler_word = None

            for card in cards.values():
                if card.is_new:
                    filler_word = card
                    break

            if filler_word:
                filler_word.is_new = False
                history.append(filler_word.word)
                total_words_reviewed += 1
                continue
            else:
                all_learned = True

                for card in cards.values():
                    if not card.is_learned(max_repetitions):
                        all_learned = False
                        break

                if all_learned:
                    break

        for card in due_words:
            print(f'Appending: {card.word}')
            history.append(card.word)
            card.update_word()
            total_words_reviewed += 1

    write_words_to_csv(history, 'history.csv')
    print('All cards appended!')
    print(f'Length: {len(history)}')
    
if __name__ == '__main__':
    cards = load_words_from_json('definitions.json')
    review_session(cards)