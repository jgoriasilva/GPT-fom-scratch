from typing import *
from model import Tokenizer


def get_vocab(input_file_name: str) -> List[str]:
    with open(input_file_name, mode='r', encoding='UTF-8') as f:
        text = f.read()
    vocab = list(set(text))
    return vocab


def test_tokenizer(tokenizer: Tokenizer, input_file_name: str) -> None:
    with open(input_file_name, mode='r', encoding='UTF-8') as f:
        text = f.read()
    tokens = tokenizer.encode(text)
    print(tokens)
    text = tokenizer.decode(tokens)
    print(text)


def main() -> None:
    input_file_name = 'input 2.txt'
    vocab = get_vocab(input_file_name)
    tokenizer = Tokenizer(vocab)

    test_tokenizer(tokenizer, input_file_name)


if __name__ == '__main__':
    main()