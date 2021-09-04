"""
# 编写一个程序，它将找到所有这些数字，可被7整除，但不是5的倍数，2000至3200(包括在内)。得到的数字应按逗号分隔的顺序打印在一行上。

l = []
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        l.append(str(i))  # 元素必须转为字符串格式
print(','.join(l))




# 编写一个可以计算给定数的阶乘的程序（n*(n*1)*...*2*1）。结果应该以逗号分隔的顺序打印在一行上。假设向程序提供以下输入:8  则输出为:40320

def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x - 1)


print("请输入一个数字：")
x = int(input())
print(fact(x))


# 问题:使用给定的整数n，编写一个程序生成一个包含(i, i*i)的字典，该字典包含1到n之间的整数(两者都包含)。然后程序应该打印字典。
# 假设向程序提供以下输入:8
# 则输出为:{1:1，2:4，3:9，4:16，5:25，6:36，,7:49，8:64}

print("请输入一个数字：")
n = int(input())
d = dict()  # 创建一个空字典
for i in range(1, n + 1):
    d[i] = i * i
print(d)

# 问题:编写一个程序，该程序接受控制台以逗号分隔的数字序列，并生成包含每个数字的列表和元组。假设向程序提供以下输入:
# 34岁,67年,55岁,33岁,12日,98年
# 则输出为:['34'， '67'， '55'， '33'， '12'， '98']
#        ('34'， '67'， '55'， '33'， '12'， '98')

import re

print("请输入一组数字：")
value = input()
l = value.split(",")
k = re.findall(r'[0-9]+', value)
t = tuple(k)
print(k)
print(t)



# 问题:定义一个至少有两个方法的类: getString:从控制台输入获取字符串  printString::打印大写母的字符串。

class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        print("请输入字符串：")
        self.s = input()

    def printString(self):
        print(self.s.upper())


strobj = InputOutString()
strobj.getString()
strobj.printString()


# 编写一个程序，根据给定的公式计算并打印值:Q=\sqrt{[(2*C*D)/H]}。以下是C和H的固定值:C是50。H是30。D是一个变量，它的值应该以逗号分隔的序列输入到程序中。
# 例子假设程序的输入序列是逗号分隔的:100，150，180，
# 程序输出为:18，22，24
import math

c = 50
h = 30
value = []
print("请输入数据：")
items = [x for x in input().split(',')]
# 删除空元素
while '' in items:
    items.remove('')
print(items)
for i in items:
    value.append(str(int(round(math.sqrt(2 * c * float(i) / h)))))  # round 四舍五入

print(",".join(value))



# 问题:编写一个程序，以2位数字，X,Y作为输入，生成一个二维数组。数组的第i行和第j列中的元素值应该是i*j。
# 注意:i= 0,1 . .,X - 1;    j = 0, 1,­Y-1。
# 例子假设程序有以下输入:3、5
# 则程序输出为:[[0,0,0,0,0],[0,1,2,3,4],[0,2,4,6,8]]

print('请输入两个数字：')
input_str = input()
dimensions = [int(x) for x in input_str.split(',')]
rowNum = dimensions[0]
colNum = dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col] = row * col
print(multilist)

# 编写一个程序，接受逗号分隔的单词序列作为输入，按字母顺序排序后按逗号分隔的序列打印单词。假设向程序提供以下输入:
# without,hello,bag,world
# 则输出为:
# bag,hello,without,world

print("请输入一组字符串：")
items = [x for x in input().split(',')]
items.sort()
print(','.join(items))


# 编写一个程序，接受一行序列作为输入，并在将句子中的所有字符大写后打印行。
print("请输入一组字符串：")


def func():
    lines = []
    while True:
        s = input()
        if s:
            lines.append(s.upper())
        else:
            break

    for sentence in lines:
        print(sentence)


func()

# 编写一个程序，接受一系列空格分隔的单词作为输入，并在删除所有重复的单词并按字母数字排序后打印这些单词

print("请输入一组单词：")
s = input()
words = [word for word in s.split(" ")]
print(' '.join(sorted(list(set(words)))))


# 编写一个程序，接受一系列逗号分隔的4位二进制数作为输入，然后检查它们是否可被5整除。可被5整除的数字将以逗号分隔的顺序打印。
# 例：0100,0011,1010,1001
# 那么输出应该是： 1010

value = []
print("请输入逗号分隔的4位二进制数：")
items = [x for x in input().split(',')]
for i in items:
    inti = int(i, 2)
    if inti % 5 == 0:
        value.append(i)
    else:
        continue

print(','.join(value))

# 编写一个程序，它将找到1000到3000之间的所有这些数字（均包括在内），这样数字的每个数字都是偶数。
# 获得的数字应以逗号分隔的顺序打印在一行上。

values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0) and (int(s[3]) % 2 == 0):
        values.append(s)
print(",".join(values))


# 编写一个接受句子并计算字母和数字的程序。假设为程序提供了以下输入：
# Hello world! 123
# 然后，输出应该是：
# 字母10
# 数字3
print("请输入一句话：")
count_a = 0
count_d = 0
items = input()
for i in items:
    if i.isdigit():
        count_d += 1
    elif i.isalpha():
        count_a += 1
    else:
        continue
print(f"字母：{count_a}")
print(f"数字：{count_d}")


# 题：编写一个接受句子的程序，并计算大写字母和小写字母的数量。
# 假设为程序提供了以下输入：
# Hello world!
# 然后，输出应该是：
# 大写实例 1
# 小写实例 9

print("请输入一句话：")
count_u = 0
count_l = 0
items = input()
for i in items:
    if i.isupper():
        count_u += 1
    elif i.islower():
        count_l += 1
    else:
        continue
print(f"大写实例：{count_u}")
print(f"小写实例：{count_l}")


# 题：编写一个程序，计算a + aa + aaa + aaaa的值，给定的数字作为a的值。假设为程序提供了以下输入：
# 9  然后，输出应该是： 11106

print("请输入一个整数n:")
n = input()
s1 = int(n)
s2 = int(str(f'{n}{n}'))
s3 = int(str(f'{n}{n}{n}'))
s4 = int(str(f'{n}{n}{n}{n}'))
print(s1 + s2 + s3 + s4)


# 题：使用列表推导来对列表中的每个奇数。 该列表由一系列逗号分隔的数字输入。
# 假设为程序提供了以下输入：
# 1,2,3,4,5,6,7,8,9
# 然后，输出应该是：
# 1,3,5,7,9
print("请输入一列逗号分隔的数字")
l = []
for i in input().split(','):
    if int(i) % 2 == 1:
        l.append(i)
print(','.join(l))

values = input()
numbers = [x for x in values.split(",") if int(x)%2!=0]
print (",".join(numbers))

"""
# 题：编写一个程序，根据控制台输入的事务日志计算银行帐户的净金额。 事务日志格式如下所示：
# D 100
# W 200
# D表示存款，而W表示提款。
# 假设为程序提供了以下输入：
# D 300
# D 300
# W 200
# D 100
# 然后，输出应该是：
# 500
import re

netAmount = 0
print("请输入：")
while True:
    s = input()
    if not re.findall('^(W|D)\s*\d+', s):
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation == "D":
        netAmount += amount
    elif operation == "W":
        netAmount -= amount
    else:
        pass
print(netAmount)
