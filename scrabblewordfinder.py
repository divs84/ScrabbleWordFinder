import sys
from typing import List

class ScrabbleWordFinder:
    
    def __init__(self, rack: str):
        self.scores = {"A": 1, "C": 3, "B": 3, "E": 1,  "D": 2, "G": 2,
                       "F": 4, "I": 1, "H": 4, "K": 5,  "J": 8, "M": 3,
                       "L": 1, "O": 1, "N": 1, "Q": 10, "P": 3, "S": 1,
                       "R": 1, "U": 1, "T": 1, "W": 4,  "V": 4, "Y": 4,
                       "X": 8, "Z": 10}  
        self.word_list = {}
        self.rack = rack.upper()


    def load_word_list(self, filename: str) -> List:
        """
        Load a tab-separated word list from a given filename.

        Keyword arguments:
        filename -- the filename containing the word list.
        """
        f = open(filename, 'r')
        for line in f.readlines():
            word, definition = line.strip().split('\t')
            self.word_list[word] = definition


    def can_make_word(self, word: str) -> bool:
        """
        Check to see if a given word can be made with the
        letters on the rack.

        Keyword arguments:
        word -- the word to check to see if it can be spelled
                with the rack letters.
        """
        rack_letters = list(self.rack)
        for letter in word:
            if letter in rack_letters:
                rack_letters.remove(letter)
            elif '*' in rack_letters:
                rack_letters.remove('*')
            else:
                return False
        return True


    def find_words(self):
        """
        Find all valid words that can be spelt with the
        rack letters.  Return a list containing each valid word,
        its scrabble score, and its definition.
        """
        valid_words = []
        for word in self.word_list:
            if self.can_make_word(word):
                total_score = 0
                for letter in word:
                    total_score += self.scores[letter]
                valid_words.append([total_score, word, self.word_list[word]])

        return valid_words


def main(rack_letters):
    
    swf = ScrabbleWordFinder(rack_letters)
    swf.load_word_list("word_list.txt")
    valid_words = swf.find_words()

    print(f"{'Score':^5} {'Word':^10} {'Definition':<50}")
    [print(f"{valid[0]:^5} {valid[1]:<10} {valid[2]:<50}") for valid in valid_words]
    

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        main(sys.argv[1])
    else:
        print("Invalid number of arguments specified.")