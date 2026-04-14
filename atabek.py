def reverse_words(sentence: str) -> str:
    words = sentence.strip().split()
    return ' '.join(reversed(words))
    
def main():
    print("=== Программа: Обратный порядок слов ===")
    print("Введите 'выход' (или 'exit') для завершения работы.\n")
