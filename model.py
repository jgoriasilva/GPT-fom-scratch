import enum
from typing import *

class Tokenizer():
    def __init__(self, vocab: List[str]):
        self.vocab = vocab
        self.vocab_size = len(vocab)
    
    def encode(self, text: List[str]) -> List[int]:
        string_to_int = {s: i for i, s in enumerate(self.vocab)}
        return [string_to_int[s] for s in text]

    def decode(self, tokens: List[int]) -> List[str]:
        int_to_string = {i: s for i, s in enumerate(self.vocab)}
        return ''.join([int_to_string[i] for i in tokens])