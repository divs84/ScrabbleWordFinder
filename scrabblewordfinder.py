from englishletterscores import EnglishLetterScores
from letterscores import LetterScores
import sys
from typing import List
from word import Word

class ScrabbleWordFinder:
    
    letter_set: LetterScores
    word_list: List[Word]
    rack: str

    def __init__(self, letter_set: LetterScores, rack: str) -> None:
        self.letter_set = letter_set
        self.word_list = []
        self.rack = rack.upper()


    def load_word_list(self, filename: str) -> None:
        """
        Load a tab-separated word list from a given filename.

        Keyword arguments:
        filename -- the filename containing the word list.
        """
        f = open(filename, 'r')
        for line in f.readlines():
            word, definition = line.strip().split('\t')
            self.word_list.append(Word(word, definition, self.letter_set))

        return


    def can_make_word(self, word: Word) -> bool:
        """
        Check to see if a given word can be made with the
        letters on the rack.

        Keyword arguments:
        word -- the word to check to see if it can be spelled
                with the rack letters.
        """
        rack_letters = list(self.rack)
        for idx, letter in enumerate(word.letters):
            if letter in rack_letters:
                rack_letters.remove(letter)
            elif '*' in rack_letters:
                rack_letters.remove('*')
                word.set_wildcard(idx)
            else:
                return False
        return True


    def find_words(self) -> List:
        """
        Find all valid words that can be spelt with the
        rack letters.  Return a list containing each valid word,
        its scrabble score, and its definition.
        """
        valid_words = []
        for word in self.word_list:
            if self.can_make_word(word):    
                valid_words.append(word)
        return valid_words


def main(rack_letters):
    
    swf = ScrabbleWordFinder(EnglishLetterScores(), rack_letters)
    swf.load_word_list("english_word_list.txt")
    valid_words = swf.find_words()
    
    [print(word) for word in valid_words]
    

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        main(sys.argv[1])
    else:
        print("Invalid number of arguments specified.")