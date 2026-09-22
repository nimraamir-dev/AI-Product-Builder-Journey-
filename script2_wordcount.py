with open("sample.txt", "r") as file:
    content = file.read()

words = content.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1
print(word_count)