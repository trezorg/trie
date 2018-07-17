class BruteForce:

    def __init__(self):
        self.store = []

    def add_word(self, word):
        self.store.append(word)

    def get_words_count(self, word):
        return sum(1 for wrd in self.store if wrd.startswith(word))
