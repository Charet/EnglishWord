import random
import os
import platform

platform = platform.system()
ture_word = []
false_word = []
word = []


def random_english(length, word):

    while length != 0:
        number = random.randint(1, length)

        number = number*2-1
        print(word[number])

        input_word = input()

        if platform == "Windows":
            os.system('cls')
        elif platform == "Linux":
            os.system('clear')

        if input_word == word[number-1]:
            ture_word.append(input_word + ' ' + word[number])
            del word[number-1:number+1]
        else:
            false_word.append(input_word + ' ' + word[number])
            del word[number-1:number+1]

        length -= 1


with open("./tmp/english.txt", "r", encoding='utf-8') as f:
    for line in f:
        lines_english = ' '.join(line.split(' ',)[0:-1])
        lines_chinese = ''.join(line.split(' ',)[-1])

        word.append(lines_english)
        word.append(lines_chinese.replace("\n", ""))


length = len(word)/2  # 计算单词总数

random_english(length, word)

print('======错误的单词======')

for i in false_word:

    print(i)

print('======正确的单词=======')

for i in ture_word:

    print(i)
