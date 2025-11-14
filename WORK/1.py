text = input("введите текст: ")
banner = input("введите запрещеные слова через запятую: ").lower().split()
banner = [word.strip() for word in banner]

words = text.split()
for i in range (len(words)):
    if words[i].lower().strip('.,!?') in banner:
        words[i] = "***"
new_text = " ".join(words)
print("\n0тредактированый текст: ")
print(new_text)