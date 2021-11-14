from typing import List
from letterscores import LetterScores

class Word:
    letters: str
    uses_wildcard: bool
    wildcard_index: int
    definition: str
    letter_set: LetterScores

    def __init__(self, word, definition, letter_set, uses_wildcard = False, wildcard_index = 0) -> None:
        self.letters = word
        self.definition = definition
        self.uses_wildcard = uses_wildcard
        self.wildcard_index = wildcard_index
        self.letter_set = letter_set

    
    def __str__(self):
        return f"{self.score():^5} {self.letters:<10} {self.definition:<50}"


    def score(self) -> int:
        word_score = 0
        for idx, letter in enumerate(self.letters):
            if self.uses_wildcard and self.wildcard_index == idx:
                continue
            word_score += self.letter_set.scores[letter]
        return word_score

    def set_wildcard(self, index) -> None:
        self.uses_wildcard = True
        self.wildcard_index = index
        return