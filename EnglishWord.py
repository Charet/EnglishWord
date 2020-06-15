import random

import os

ture_word = []

false_word = []

word = []

def random_english(length,word):

    while length != 0:

        number = random.randint(1,length)

        # print(number)

        number = number*2-1

        print(word[number])

        input_word = input()

        # print(word)

        os.system('cls')

        if input_word == word[number-1]:

            ture_word.append(input_word + ' ' + word[number])

            # print(number-1,number+1)

            del word[number-1:number+1]

            # print(word)

        else:

            false_word.append(input_word + ' ' + word[number])

            # print(number-1,number+1)

            del word[number-1:number+1]

            # print(word)

        # print(false_word)

        length-=1

for line in open("./tmp/english.txt","r",encoding = 'utf-8'):

    # print(line)

    lines_english = ' '.join(line.split(' ',)[0:-1])

    lines_chinese = ''.join(line.split(' ',)[-1])

    word.append(lines_english)

    word.append(lines_chinese.replace("\n",""))

# print(word)

length = len(word)/2 #计算单词总数

random_english(length,word)

print('======错误的单词======')

for i in false_word:

    print(i)

print('======正确的单词=======')

for i in ture_word:

    print(i)

input()
