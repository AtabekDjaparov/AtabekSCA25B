def reverse_words(sentence: str) -> str:
    words = sentence.strip().split()
    return ' '.join(reversed(words))
