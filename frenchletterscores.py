from letterscores import LetterScores

class FrenchLetterScores(LetterScores):

    def __init__(self):
        self.scores = {"A": 1,  "C": 2, "B": 3, "E": 1,  "D": 2, "G": 2,
                       "F": 4,  "I": 1, "H": 4, "K": 10, "J": 8, "M": 2,
                       "L": 1,  "O": 1, "N": 1, "Q": 8,  "P": 3, "S": 1,
                       "R": 1,  "U": 1, "T": 1, "W": 10, "V": 4, "Y": 10,
                       "X": 10, "Z": 10}  
        