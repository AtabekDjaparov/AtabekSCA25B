def reverse_words(sentence: str) -> str:
    words = sentence.strip().split()
    return ' '.join(reversed(words))

def main():
    print("=== Программа: Обратный порядок слов ===")
    print("Введите 'выход' (или 'exit') для завершения работы.\n")
    
    while True:
        user_input = input("Введите предложение: ")
        if user_input.lower() == 'выход' or user_input.lower() == 'exit':
            print("Завершение работы программы. До свидания!")
            break
        if not user_input.strip():
            print("Ошибка: Предложение не может быть пустым. Попробуйте еще раз.\n")
            continue
        result = reverse_words(user_input)
        print(f"Результат: {result}\n")

if __name__ == "__main__":
    main()