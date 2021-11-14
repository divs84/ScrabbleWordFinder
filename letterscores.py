from abc import ABC

class LetterScores(ABC):
    scores = { }

    def __init__(self) -> None:
        super().__init__()