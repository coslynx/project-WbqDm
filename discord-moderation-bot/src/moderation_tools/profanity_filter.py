import json

class ProfanityFilter:
    def __init__(self):
        self.banned_words = []

    def load_banned_words(self, file_path):
        try:
            with open(file_path, 'r') as file:
                self.banned_words = json.load(file)
        except FileNotFoundError:
            print("Error: Banned words file not found.")
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in banned words file.")

    def add_banned_word(self, word):
        self.banned_words.append(word)

    def remove_banned_word(self, word):
        if word in self.banned_words:
            self.banned_words.remove(word)
        else:
            print("Error: Word is not in the list of banned words.")

    def filter_message(self, message):
        clean_message = message
        for word in self.banned_words:
            clean_message = clean_message.replace(word, '*' * len(word))
        return clean_message

    def save_banned_words(self, file_path):
        try:
            with open(file_path, 'w') as file:
                json.dump(self.banned_words, file, indent=4)
        except:
            print("Error: Failed to save banned words to file.")