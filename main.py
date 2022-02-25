import random
import os
import time
import pyttsx3

true_word = []
false_word = []
word = {}


def readWord(words):  # 朗读代码
    engine = pyttsx3.init()
    engine.say(words)
    print(words)
    engine.runAndWait()  # 无此句将无法发音


def randomWord(length):  # 随机抽取单词
    serial = random.randint(1, length)
    words = list(word.keys())[serial]
    return words


def compare(words):
    print(words)
    input_word = input()
    os.system('cls')
    if input_word == word[words]:
        print("正确!")
        true_word.append(word[words] + ' ' + input_word)
        del word[words]
        time.sleep(1)
    else:
        print("错误!正确单词为:", word[words])
        false_word.append(words + ' ' + input_word)
        del word[words]
        time.sleep(5)


def openfile(file):  # 在本地文件中获取要听写的单词表
    for line in open("./words/" + file, "r", encoding='utf-8'):
        lines_english = ' '.join(line.split(' ', )[0:-1])
        lines_chinese = ''.join(line.split(' ', )[-1])
        word[lines_chinese.replace("\n", "")] = lines_english


def unit():
    print(os.listdir('./words'))
    return input("请选择听写的单词文件:")


def main():
    openfile(unit())
    length = len(word)  # 计算单词总数
    while length != 0:
        compare(randomWord(length))
        length -= 1
    print('======错误的单词======')
    for i in false_word:
        print(i)
    print('======正确的单词=======')
    for i in true_word:
        print(i)


if __name__ == '__main__':
    main()
    input()
