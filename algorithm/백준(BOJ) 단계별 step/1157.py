import sys

word = (sys.stdin.readline()).upper()
words_list = list(set(word))

words_count = []

for words in words_list:

    words_count.append(word.count(words))

if words_count.count(max(words_count)) > 1:
    print("?")

else:
    print(words_list[words_count.index((max(words_count)))])
