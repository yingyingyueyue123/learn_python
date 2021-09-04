"""
# 题：网站要求用户输入用户名和密码进行注册。编写程序以检查用户输入的密码的有效性。
# 以下是检查密码的标准：
# 1. [a-z]之间至少有1个字母
# 2. [0-9]之间至少有1个数字
# 1. [A-Z]之间至少有一个字母
# 3. [$＃@]中至少有1个字符
# 4.最短交易密码长度：6
# 5.交易密码的最大长度：12
# 您的程序应接受一系列逗号分隔的密码，并将根据上述标准进行检查。将打印符合条件的密码，每个密码用逗号分隔。
# 例：如果以下密码作为程序的输入：
#
# ABd1234@1,a F1#,2w3E*,2We3345
# 然后，程序的输出应该是：
#
# ABd1234@1
import re

value = []
print("请输入")
items = [x for x in input().split(",")]
for p in items:
    if len(p) < 6 or len(p) > 12:
        continue
    if not re.search("[a-z]", p):
        continue
    elif not re.search("[0-9]", p):
        continue
    elif not re.search("[A-Z]", p):
        continue
    elif not re.search("[$#@]", p):
        continue
    elif re.search("\s", p):
        continue
    value.append(p)
print(",".join(value))

# 题：您需要编写一个程序，按升序对（名称，年龄，分数）元组进行排序，其中name是字符串，age和height是数字。 元组由控制台输入。 排序标准是：
# 1：根据名称排序;
# 2：然后根据年龄排序;
# 3：然后按分数排序。
# 优先级是name> age>得分。
# 如果给出以下元组作为程序的输入：
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# 然后，程序的输出应该是：
# [（'John'，'20'，'90'），（'Jony'，'17'，'91'），（'Jony'，'17'，'93'），（'Json'，'21 '，'85'），（'Tom'，'19'，'80'）]
from operator import itemgetter, attrgetter

l = []
print("请输入：")
while True:
    s = input()
    if not s:
        break
    l.append(tuple(s.split(",")))
print(sorted(l, key=itemgetter(0, 1, 2)))



# 题：使用生成器定义一个类，该生成器可以在给定范围0和n之间迭代可被7整除的数字。

def putNumber(n):
    i = 0
    while i < n:
        j = i
        i = i + 1
        if j % 7 == 0:
            yield j


for i in putNumber(100):
    print(i)

for i in range(0, 101, 7):
    print(i)

# 机器人从原点（0,0）开始在平面中移动。 机器人可以通过给定的步骤向上，向下，向左和向右移动。 机器人运动的痕迹如下所示：
# UP 5
# DOWN 3
# LETF 3
# RIGHT 2
# 方向之后的数字是步骤。 请编写一个程序来计算一系列运动和原点之后距当前位置的距离。如果距离是浮点数，则只打印最接近的整数。
# 例：如果给出以下元组作为程序的输入：
# UP 5
# DOWN 3
# LETF 3
# RIGHT 2
# 然后，程序的输出应该是：2
import math

print("请输入：")
w = 0
w1 = 0
w2 = 0
while True:
    s = input()
    if not s:
        break
    values = s.split(" ")
    fx = values[0]
    num = int(values[1])
    if fx == "UP":
        w1 += num
    elif fx == "DOWN":
        w1 -= num
    elif fx == "LETF":
        w2 += num
    elif fx == "RIGHT":
        w2 -= num
    else:
        continue
w = int(round(math.sqrt(w1 ^ 2 + w2 ^ 2)))
print(w)

# 题：编写一个程序来计算输入中单词的频率。 按字母顺序对键进行排序后输出。
# 假设为程序提供了以下输入：
#
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
#
# 然后，输出应该是：
#
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1
freq = {}
print("请输入：")
words = input().split(" ")
for word in words:
    # 字典get(key，default)，返回指定键的值，如果键不在字典中返回默认值 None 或者设置的默认值。
    freq[word] = freq.get(word, 0) + 1
for i in sorted(freq.keys()):
    print(f'{i}:{freq[i]}')



# 题：写一个可以计算数字平方值的方法
def func(x):
    return (x ** 2)


print(func(10))

# 题：Python有许多内置函数，如果您不知道如何使用它，您可以在线阅读文档或查找一些书籍。 但是Python为每个内置函数都有一个内置的文档函数。
# 请编写一个程序来打印一些Python内置函数文档，例如abs（），int（），raw_input（）
# 并为您自己的功能添加文档
# 提示：内置文档方法是__doc__
print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)


def square(num):
    return num ** 2


print(square(2))
print(square.__doc__)

"""


# 题：定义一个类，它具有类参数并具有相同的实例参数。
# 提示：定义一个实例参数，需要在__init__方法中添加它。您可以使用构造参数初始化对象，也可以稍后设置该值
class Person:
    name = "yueyue"

    def __init__(self, name=None):
        self.name = name


lily = Person("lily")
print(Person.name, lily.name)
yoyo = Person()
yoyo.name = "yoyo"
print(Person.name, yoyo.name)
