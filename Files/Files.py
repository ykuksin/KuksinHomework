print("Несовпадающие строки: ")
text1_file = open("text1")
text2_file = open("text2")
line = 0
for text1, text2 in zip(text1_file, text2_file):
    line += 1
    if text1 != text2:
        print(f"Номер строки: {line}")
        print(f"{text1=}, {text2=}")
text1_file.close()
text2_file.close()


print()
print("Статистика файла:")
text_stat = {
    "line_count": 0,
    "symbol_count": 0,
    "vowels_count": 0,
    "consonants_count": 0,
    "digits_count": 0,
}
with open("text") as text_file:
    for line in text_file:
        text_stat["symbol_count"] += len(line)
        text_stat["line_count"] += 1
        for symbol in line:
            if symbol in "eyuioa":
                text_stat["vowels_count"] += 1
            elif symbol in "qwrtpsdfghjklzxcvbnm":
                text_stat["consonants_count"] += 1
            elif symbol in "1234567890":
                text_stat["digits_count"] += 1
with open("stat", "w+") as file_stat:
    for key in text_stat:
        print(key, text_stat[key], file=file_stat)
    file_stat.seek(0)
    print(file_stat.read())


print("Длина самой большой строки: ")
longest_line_len = 0
with open("text") as text_file:
    for line in text_file:
        if len(line) > longest_line_len:
            longest_line_len = len(line)
print(longest_line_len)





