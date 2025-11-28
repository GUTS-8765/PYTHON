while True:
    text = input("введите текст: ")
    sentences_count = sum(text.count(char) for char in ['.', '!', '?'])
    print(f"В данном тексте {sentences_count} предложений.\n")