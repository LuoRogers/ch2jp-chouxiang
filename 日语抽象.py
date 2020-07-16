# copyright Bilibili@Rogersだ
# 功能：尽可能的将汉字抽象为日语平假名。
# 使用方法：1：在python文件同一目录下创建“text.txt”文件，并在其中写入中文汉字。
#         2：运行python程序
#         3：打开刚刚的文件夹内的“text—to.txt”文件查看结果。
# 注意:本程序依赖于"pypinyin"库，请运行前安装。

import re
from pypinyin import lazy_pinyin
chja = {
    "a":"あ",
    "yi":"い",
    "wu":"う",
    "o":"お",
    "ka":"か",
    "ku":"く",
    "ga":"が",
    "gu":"ぐ",
    "xi":"し",
    "si":"す",
    "suo":"そ",
    "za":"ざ",
    "ji":"じ",
    "zi":"ず",
    "zuo":"ぞ",
    "ta":"た",
    "qi":"ち",
    "ci":"つ",
    "tuo":"と",
    "na":"な",
    "ni":"に",
    "nu":"ぬ",
    "nuo":"の",
    "ha":"は",
    "fu":"ふ",
    "huo":"ほ",
    "ba":"ば",
    "bi":"び",
    "bu":"ぶ",
    "bo":"ぼ",
    "pa":"ぱ",
    "pi":"ぴ",
    "pu":"ぷ",
    "po":"ぽ",
    "ma":"ま",
    "mi":"み",
    "mo":"も",
    "ya":"や",
    "yiu":"ゆ",
    "yo":"よ",
    "wa":"わ",
    "xia":"しゃ",
    "xiu":"しゅ",
    "qia":"ちゃ",
    "qiu":"ちゅ",
    "niu":"にゅ",
    "liu":"りゅ",
    "jia":"じゃ",
    "jiu":"じゅ",
    "biu":"びゅ",
    "yin":"いん",
    "kan":"かん",
    "kang":"かん",
    "gan":"がん",
    "gang":"がん",
    "xin":"しん",
    "xing":"しん",
    "zan":"ざん",
    "jin":"じん",
    "jing":"じん",
    "tan":"たん",
    "tang":"たん",
    "qin":"ちん",
    "qing":"ちん",
    "tuo":"とん",
    "nan":"なん",
    "nang":"なん",
    "nin":"にん",
    "ning":"にん",
    "han":"はん",
    "bang":"ばん",
    "bin":"びん",
    "bing":"びん",
    "bong":"ぼん",
    "ban":"びん",
    "pang":"ぱん",
    "pin":"ぴん",
    "ping":"ぴん",
    "pong":"ぽん",
    "mang":"まん",
    "man":"まん",
    "ming":"みん",
    "min":"みん",
    "mong":"もん",
    }

with open("text.txt") as f:
    han = f.read()
# print(han)

# han = input("请输入汉字:")
# print(pinyin)
i = 0
sentence = ''
for word in han:
    ja = chja.get(lazy_pinyin(word)[0])
    if ja == None or re.fullmatch('[a-z]',word):
        ja = word
    sentence = sentence + str(ja)
    i = i + 1
# print(sentence)
with open("text_to.txt","w") as tto:
    tto.write(sentence)
print("抽象完成")
