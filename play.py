import json
import csv

def load_words_from_csv(path):
    with open(path, 'r') as f:
        reader = csv.reader(f)

        words = []

        for row in reader:
            if row:
                words.append(row[0])

        return words
    
def load_definitions_from_json(path):
    with open(path, 'r') as f:
        definitions = json.load(f)

    return definitions

def test(words, definitions):
    top_score = 0
    encounter_words = set()

    for word in words:
        print('\n' + '-' * 10)
        print(f'\nWord: {word}')

        if word not in definitions:
            print('Definition not found for this word. Skipping...')

        definition = definitions[word]

        if word not in encounter_words:
            print('\nNew word...')
            print(f'\nWord: {word}')
            print(f'Definition: {definition}')

        user_input = input('\nCould you recall the definition? Be honest! (Y/N): ')

        if user_input == 'Y' or user_input == 'y':
            encounter_words.add(word)
            top_score += 1
            print('\nNice!')
        else:
            print('\nGame over!')
            print(f'Top score: {top_score}')
            print(f'Failed word: {word}')
            print(f'Correct definition: {definition}')

            return
    
    print('\nCongratulations! You have completed the game.')
    print(f'Top score: {top_score}')

if __name__ == '__main__':
    words = load_words_from_csv('history.csv')
    definitions = load_definitions_from_json('definitions.json')

    print('\nWelcome to the word definition game! The objective of the game is to define as many words as possible.')

    test(words, definitions)