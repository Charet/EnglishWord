import random
import os
import time
import pyttsx3
import keyboard

true_word = []
false_word = []
word = []


def readWord(key, words):  # 朗读代码
    if key.event_type == 'up' and key.name == 'space':
        engine = pyttsx3.init()
        engine.say(words)
        engine.runAndWait()  # 无此句将无法发音


def randomWord(length):  # 随机抽取单词
    serial = random.randint(1, length)
    serial = serial * 2 - 1
    return serial


def compare(serial):
    print(word[serial])
    input_word = input()
    os.system('cls')
    if input_word == word[serial - 1]:
        print("正确!")
        true_word.append(word[serial] + ' ' + input_word)
        del word[serial - 1:serial + 1]
        time.sleep(1)
    else:
        print("错误!正确单词为:", word[serial - 1], "\n按空格可以朗读此单词\n按Enter可进入下一个单词")
        false_word.append(word[serial] + ' ' + input_word)
        del word[serial - 1:serial + 1]
        keyboard.add_hotkey('space', readWord, args=(word[serial - 1],))
        keyboard.wait("enter")


def openfile(file):  # 在本地文件中获取要听写的单词表
    for line in open("./words/" + file, "r", encoding='utf-8'):
        lines_english = ' '.join(line.split(' ', )[0:-1])
        lines_chinese = ''.join(line.split(' ', )[-1])
        word.append(lines_english)
        word.append(lines_chinese.replace("\n", ""))


def unit():
    print(os.listdir('./words'))
    return input("请选择听写的单词文件:")


def main():
    openfile(unit())
    length = len(word) / 2  # 计算单词总数
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
